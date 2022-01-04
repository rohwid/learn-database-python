from logging import debug
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# Import from __init__
from app.api    import (db, create_app)
from app        import blueprint
from app.api    import db_graph

# postgres dialect sqlalchemy
from sqlalchemy.dialects.postgresql import insert

from app.api.model import User
from app.api.model import Role
from app.api.model import Permission
from app.api.model import Vertex, Edge, Gatra, OAuth2Client

from app.config.entity import VERTEX_LIST, EDGE_LIST, GATRA_LIST

app = create_app(os.getenv("ENVIRONMENT") or 'dev')
app.register_blueprint(blueprint, url_prefix="/v1")


app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    """ function to start flask apps"""
    host = os.getenv("HOST") or '127.0.0.1'
    app.run(host=host, debug=True,  use_evalex=False)

@manager.command
def init():
    """ create init function here """
    #create vertex
    vertex_query = insert(Vertex).values(VERTEX_LIST).on_conflict_do_nothing()
    db.session.execute(vertex_query)
    #create edge
    edge_query = insert(Edge).values(EDGE_LIST).on_conflict_do_nothing()
    db.session.execute(edge_query)
    #create gatra
    gatra_query = insert(Gatra).values(GATRA_LIST).on_conflict_do_nothing()
    db.session.execute(gatra_query)

    #Create user admin
    admin_email = os.getenv("ADMIN_EMAIL", "Admin_Pacmann") 
    # only create when admin not exist!
    admin = User.query.filter_by(email=admin_email).first()
    if not admin:
        admin = User(
            username="ADMIN",
            email=admin_email
        )
        admin.set_password(os.getenv("ADMIN_PASSWORD", "password"))
        db.session.add(admin)
    db.session.commit()

    #generate oauth client
    oauth_client = OAuth2Client.query.filter_by(user_id=admin.id).first()
    if not oauth_client:
        client_id = os.getenv("OAUTH_CLIENT_ID", "d239jmJasdddj902djd32")
        client_secret = os.getenv("OAUTH_CLIENT_SECRET", "d239jmJasdddj902djd32akd0239adq2dk30k0-") 
        params = {
            "user_id" : admin.id,
            "client_name": "admin",
            "client_uri": "https://ntxdemo.io/",
            "grant_type": ["client_credentials"],
            "redirect_uri": ["https://ntxdemo.io/"],
            "response_type": ["code"],
            "scope": "all_access",
            "token_endpoint_auth_method": "client_secret_basic"
        }
        OauthClientServices(user_id=admin.id, client_id=client_id, client_secret=client_secret).add(params)

    #alter db graph configuration
    db_graph.client.command("alter database custom standardElementConstraints = false")

@manager.command
def role_permission_upgrade():
    """ create role_permission upgrade function here """
    #INSERT ROLE
    role = Role.query.all()
    role = [r.name for r in role]
    role = list(set(list(PERMISSION.values())) - set(role))
    role = [{"name" : r} for r in role]
    if len(role) > 0:
        db.session.execute(insert(Role).values(role).on_conflict_do_nothing())
        db.session.commit()

    #INSERT PERMISSION
    permission = Permission.query.all()
    permission = [p.name for p in permission]
    permission = list(set(list(PERMISSION.values())) - set(permission))
    permission = [{"name" : r} for r in permission]
    if len(permission) > 0:
        db.session.execute(insert(Permission).values(permission).on_conflict_do_nothing())
        db.session.commit()

    #INSERT ROLE PERMISSION GROUP
    for i in ROLE_PERMISSION_GROUP:
        permission = Permission.query.filter(Permission.name.in_(i['permission']), Permission.is_active==True).all()
        role = Role.query.filter_by(name=i['role'], is_active=True).first()

        for j in permission:
            role.permission.append(j)

        db.session.add(role)
        db.session.commit()


if __name__ == "__main__":
    manager.run()
