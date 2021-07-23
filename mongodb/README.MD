# CREATE DB

command :
+ use DATABASE_NAME

example :

	> use coba

# DROP DB

command :
+ use DATABASE_NAME
+ db.dropDatabase()

example :

	> use coba
	> db.dropDatabase()

# CREATE COLLECTION

command :
+ db.createCollection(name,options)
+ db.COLLECTION_NAME.insert({CONTENT})

example :

	> db.createCollection(student)
	> db.movies.insert({"name" = "batman"}) --> Create collection and insert document

# DROP COLLECTION

command :
+ db.COLLECTION_NAME.drop()


# INSERT DOCUMENT

+ db.COLLECTION_NAME.insert({CONTENT})

example 1 :

	> db.mycol.insert({ "student_id": 2209100001, "name" : "Bambang" })

example 2 :

	> db.mycol.insert({"student_id": 2209100001, "name": "Bambang"})

	> db.mycol.insert({"student_id": 2209100001, "name": "Bambang"})

	> db.mycol.insert({"student_id": 2209100001, "name": "Bambang"})

# QUERY DOCUMENT

command :
+ db.COLLECTION_NAME.find(QUERY_CRITERIA).pretty()

QUERY_CRITERIA : Equality, Less Than, Less Than Equals, Greater Than, Greater Than Equals, and etc on this [site](http://www.tutorialspoint.com/mongodb/mongodb_query_document.htm).

example :

	> db.student.find({"name": "Bambang"}).pretty()
	  {
		"_id": ObjectId("566ecc17aee8b8c10ea35cf3"),
		"student_id": 2209100001,
		"name": "Bambang"
	  }

# UPDATE DOCUMENT

command :
+ db.COLLECTION_NAME.update(SELECTIOIN_CRITERIA, UPDATED_DATA)

update single document example :

	> db.student.update({"name": "Andi"}, {$set:{"name": "Arif"}})

	> db.student.update({"name": "Andi"}, {$set:{"name": "Arif","student_id": 220910004}})

	> db.student.update({"name": "Bambang"}, {$set: {"email": "bambang@gmail.com", "criteria": ["ganteng", "kaya", "jomblo"]}})

update multiple document example :

	> db.student.update({"name": "Podo1"}, {$set:{"student_id": 2209100010, "name": "Podo Kabeh"}}, {multi: true})

replace all document with save example :

	> db.student.save({"_id": ObjectId("566ece4aaee8b8c10ea35cf4"), "student_id": 2209100002, "name": "Agus"});

# DELETE DOCUMENT

command :
+ db.COLLECTION_NAME.remove(DELLETION_CRITTERIA)
+ db.COLLECTION_NAME.remove()

Delete by criteria example :

	> db.student.remove({'student_id: 2209100001})

Delete all document or collection :

	> db.student.remove()

# PROJECTION

Projection meaning is **selecting only necessary data** rather than selecting whole of the data of a document.

command :
+ db.COLLECTION_NAME.find({},{KEY:1 or 0})

data example :

	> db.student.find({},{KEY:1})
	  { "_id": ObjectId("566ece4aaee8b8c10ea35cf4") }
	  { "_id": ObjectId("566ece54aee8b8c10ea35cf5") }
	  { "_id": ObjectId("56710117b27f148869440dee") }
	  { "_id": ObjectId("5671180abc4223602dce240b") }
	  { "_id": ObjectId("566ecc17aee8b8c10ea35cf3") }
	  { "_id": ObjectId("5671182cbc4223602dce240c") }

example :

	> db.mycol.find({},{"_id":0, "student_id":1, "name": 1}) --> 1 = true / 0 = false (only show the title)
	  { "student_id": 2209100002, "name": "Agus" }
	  { "student_id": 2209100003, "name": "Arif" }
	  { "student_id": 2209100004, "name": "Bagus" }
	  { "student_id": 2209100010, "name": "Podo Kabeh" }
	  { "student_id": 2209100001, "name": "Bambang" }
	  { "student_id": 2209100005, "name": "Nana" }

# LIMITING RECORD

To limit the records in MongoDB, you need to use limit() method. limit() method accepts one number type argument, **which is number of documents that you want to displayed**.

command :
+ db.COLLECTION_NAME.find({},{KEY:1 or 0}).limit(LIMIT NUMBER)

example :

	> db.student.find({}, {"_id":0,"student_id":1,"name":1}).limit(2)
	  { "student_id": 2209100002, "name": "Agus" }
	  { "student_id": 2209100003, "name": "Arif" }

Apart from limit() method there is one more method skip() which also accepts number type argument and used to skip number of documents.

command :
+ db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)

data example :

	{ "_id": ObjectId(5983548781331adf45ec5), "title": "MongoDB Overview"}
	{ "_id": ObjectId(5983548781331adf45ec6), "title": "NoSQL Overview"}
	{ "_id": ObjectId(5983548781331adf45ec7), "title": "Tutorials Point Overview"}

example 1 :

	> db.mycol.find({},{"title":1,_id:0}).limit(2)
	  {"title": "MongoDB Overview"}
	  {"title": "NoSQL Overview"}

example 2 :

	> db.mycol.find({},{"title":1,_id:0}).limit(1).skip(1)
	  {"title":"NoSQL Overview"}

# INDEXING

Indexes support the **efficient resolution of queries**. Without indexes, MongoDB must scan every document of a collection to select those documents that match the query statement. This scan is highly inefficient and require the mongod to process a large volume of data.

	> db.no.find({"student_id": 5}).pretty()
	  {
		"_id" : ObjectId("53c9020abcdd1ea7fb833cdf"),
		"student_id" : 5,
		"name" : "Wid"
	  }

and compare with more bigger student_id, how fast the process executed.

	> db.no.find({"student_id": 1000000}).pretty()
	  {
		"_id" : ObjectId("53c9020abcdd1ea7fb833cdf"),
		"student_id" : 1000000,
		"name" : "Wid"
	  }

Create the index, to make the process more faster.

	> db.system.indexes.find()
	  { "v" : 1, "key" : { "_id" : 1 }, "name" : "_id_", "ns" : "temp.no" }

	> db.no.ensureIndex({"student_id": 1});

	> db.system.indexes.find()
	  { "v" : 1, "name" : "_id_", "key" : { "_id" : 1 }, "ns" : "sekolah.siswa" }
	  { "v" : 1, "name" : "student_id_1", "key" : { "student_id" : 1 }, "ns" : "sekolah.siswa" }

# AGGREGATION

Aggregations operations process data records and return computed results. Aggregation operations group values from multiple documents together, and can perform a variety of operations on the grouped data to return a single result.

command :

+ db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)

data example :

	{
		_id: ObjectId(7df78ad8902c)
		title: 'MongoDB Overview',
		description: 'MongoDB is no sql database',
		by_user: 'tutorials point',
		url: 'http://www.tutorialspoint.com',
		tags: ['mongodb', 'database', 'NoSQL'],
		likes: 100
	},
	{
		_id: ObjectId(7df78ad8902d)
		title: 'NoSQL Overview',
		description: 'No sql database is very fast',
		by_user: 'tutorials point',
		url: 'http://www.tutorialspoint.com',
		tags: ['mongodb', 'database', 'NoSQL'],
		likes: 10
	},
	{
		_id: ObjectId(7df78ad8902e)
		title: 'Neo4j Overview',
		description: 'Neo4j is no sql database',
		by_user: 'Neo4j',
		url: 'http://www.neo4j.com',
		tags: ['neo4j', 'database', 'NoSQL'],
		likes: 750
	}

aggregate example :

	> db.mycol.aggregate([{$group: {_id : "$by_user", num_tutorial : {$sum : 1}}}])
	  {
		"result": [
			{
				"_id": "tutorials point",
				"num_tutorial": 2
			},
			{
				"_id": "Neo4j",
				"num_tutorial": 1
			}
		],
		"ok" : 1
	  }

There are more function beside $sum such as $avg, $min, $max, $push, addToSet and etc on this [site](http://www.tutorialspoint.com/mongodb/mongodb_aggregation.htm).
