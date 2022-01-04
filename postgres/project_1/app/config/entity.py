VERTEX = {}
VERTEX['BELIEF'] = 'BELIEF'
VERTEX['CONDITION'] = 'CONDITION'
VERTEX['DISEASE'] = 'DISEASE'
VERTEX['ECONVARIABLE'] = 'ECONVARIABLE'
VERTEX['LABEL'] = 'LABEL'
VERTEX['LEGAL'] = 'LEGAL'
VERTEX['LOC'] = 'LOC'
VERTEX['ORG'] = 'ORG'
VERTEX['PER'] = 'PER'
VERTEX['PERIOD'] = 'PERIOD'
VERTEX['POLICY'] = 'POLICY'
VERTEX['QTY'] = 'QTY'
VERTEX['REFERENT'] = 'REFERENT'
VERTEX['STATUS'] = 'STATUS'
VERTEX['TIME'] = 'TIME'
VERTEX['TITLE'] = 'TITLE'
VERTEX['GPE'] = 'GPE'
VERTEX['EVENT'] = 'EVENT'

VERTEX_INVERSE = {}
VERTEX_INVERSE['BELIEF'] = 'BELIEF'
VERTEX_INVERSE['CONDITION'] = 'CONDITION'
VERTEX_INVERSE['DISEASE'] = 'DISEASE'
VERTEX_INVERSE['ECONVARIABLE'] = 'ECONVARIABLE'
VERTEX_INVERSE['LABEL'] = 'LABEL'
VERTEX_INVERSE['LEGAL'] = 'LEGAL'
VERTEX_INVERSE['LOC'] = 'LOC'
VERTEX_INVERSE['ORG'] = 'ORG'
VERTEX_INVERSE['PER'] = 'PER'
VERTEX_INVERSE['PERIOD'] = 'PERIOD'
VERTEX_INVERSE['POLICY'] = 'POLICY'
VERTEX_INVERSE['QTY'] = 'QTY'
VERTEX_INVERSE['REFERENT'] = 'REFERENT'
VERTEX_INVERSE['STATUS'] = 'STATUS'
VERTEX_INVERSE['TIME'] = 'TIME'
VERTEX_INVERSE['TITLE'] = 'TITLE'
VERTEX_INVERSE['GPE'] = 'GPE'
VERTEX_INVERSE['EVENT'] = 'EVENT'

EDGE = {}
EDGE['bagian_dari'] = 'bagian_dari'
EDGE['pada_tempat'] = 'pada_tempat'
EDGE['pada_waktu'] = 'pada_waktu'
EDGE['memegang_jabatan'] = 'memegang_jabatan'
EDGE['melakukan'] = 'melakukan'
EDGE['bersama'] = 'bersama'
EDGE['membahas'] = 'membahas'
EDGE['berasal'] = 'berasal'
EDGE['terkena'] = 'terkena'
EDGE['menyebabkan'] = 'menyebabkan'
EDGE['berstatus'] = 'berstatus'
EDGE['berjumlah'] = 'berjumlah'
EDGE['sebagai'] = 'sebagai'
EDGE['berkerabat'] = 'berkerabat'
EDGE['mengakibatkan'] = 'mengakibatkan'


VERTEX_LIST = [
  {
    "id": "ECONVARIABLE",
    "name": "Econvariable",
    "is_default": True
  },
  {
    "id": "DISEASE",
    "name": "Disease",
    "is_default": True
  },
  {
    "id": "GPE",
    "name": "GPE",
    "is_default": True
  },
  {
    "id": "LOC",
    "name": "Location",
    "is_default": True
  },
  {
    "id": "QTY",
    "name": "QTY",
    "is_default": True
  },
  {
    "id": "BELIEF",
    "name": "Belief",
    "is_default": True
  },
  {
    "id": "REFERENT",
    "name": "Referent",
    "is_default": True
  },
  {
    "id": "ORG",
    "name": "Organization",
    "is_default": True
  },
  {
    "id": "POLICY",
    "name": "Policy",
    "is_default": True
  },
  {
    "id": "LABEL",
    "name": "Label",
    "is_default": True
  },
  {
    "id": "PER",
    "name": "Person",
    "is_default": True
  },
  {
    "id": "STATUS",
    "name": "Status",
    "is_default": True
  },
  {
    "id": "CONDITION",
    "name": "Condition",
    "is_default": True
  },
  {
    "id": "TIME",
    "name": "Time",
    "is_default": True
  },
  {
    "id": "LEGAL",
    "name": "Legal",
    "is_default": True
  },
  {
    "id": "TITLE",
    "name": "Title",
    "is_default": True
  },
  {
    "id": "PERIOD",
    "name": "Period",
    "is_default": True
  },
  {
    "id": "EVENT",
    "name": "Event",
    "is_default": True
  }
]

EDGE_LIST = [
  {
    "id": "bagian_dari",
    "name": "bagian_dari",
    "is_default": True
  },
  {
    "id": "pada_waktu",
    "name": "pada_waktu",
    "is_default": True
  },
  {
    "id": "pada_tempat",
    "name": "pada_tempat",
    "is_default": True
  },
  {
    "id": "memegang_jabatan",
    "name": "memegang_jabatan",
    "is_default": True
  },
  {
    "id": "melakukan",
    "name": "melakukan",
    "is_default": True
  },
  {
    "id": "bersama",
    "name": "bersama",
    "is_default": True
  },
  {
    "id": "membahas",
    "name": "membahas",
    "is_default": True
  },
  {
    "id": "berasal",
    "name": "berasal",
    "is_default": True
  },
  {
    "id": "terkena",
    "name": "terkena",
    "is_default": True
  },
  {
    "id": "menyebabkan",
    "name": "menyebabkan",
    "is_default": True
  },
  {
    "id": "berjumlah",
    "name": "berjumlah",
    "is_default": True
  },
  {
    "id": "sebagai",
    "name": "sebagai",
    "is_default": True
  },
  {
    "id": "berkerabat",
    "name": "berkerabat",
    "is_default": True
  },
  {
    "id": "mengakibatkan",
    "name": "mengakibatkan",
    "is_default": True
  },
  {
    "id": "berstatus",
    "name": "berstatus",
    "is_default": True
  },
  {
    "id": "anggota",
    "name": "anggota",
    "is_default": True
  }
]

GATRA_LIST = [
  {
    "id": "politik",
    "name": "Politik"
  },
  {
    "id": "ideologi",
    "name": "Ideologi"
  },
  {
    "id": "hankam",
    "name": "Hankam"
  },
  {
    "id": "ekonomi",
    "name": "Ekonomi"
  },
  {
    "id": "sosbud",
    "name": "Sosbud"
  },
  {
    "id": "misc",
    "name": "Misc"
  }
]