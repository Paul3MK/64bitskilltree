indexed = {}

lang_skills = {
    "python": "Python",
    "cpp": "C++",
    "c": "C",
    "javascript": "JavaScript",
    "java": "Java",
    "php": "PHP",
    "rust": "Rust",
    "go": "Go",
    "dart": "Dart",
    "haskell": "Haskell",
    "swift": "Swift",
    "r": "R",
    "ruby": "Ruby",
    "kotlin": "Kotlin",
    "html": "HTML",
    "css": "CSS",
    "typescript": "TypeScript",
    "bash": "Bash",
    "vba": "VBA",
    "scala": "Scala",
    "xml": "XML",
    "sql": "SQL",
    "powershell": "Powershell",
    "assembly": "Assembly",
    "matlab": "MATLAB",
    "lua": "Lua",
    "groovy": "Groovy",
    "delphi": "Delphi",
    "objective-c": "Objective-C",
    "perl": "Perl",
    "lisp": "LISP",
    "julia": "Julia",
    "clojure": "Clojure"
}

db_skills = {
    "mysql": "MySQL",
    "oracle": "Oracle",
    "sql-server": ["Microsoft SQL Server", "SQL Server"],
    "postgres": ["PostgreSQL", "Postgres"],
    "mongo": ["MongoDB", "Mongo"],
    "redis": "Redis",
    "elasticsearch": "Elasticsearch",
    "db2": ["IBM DB2", "DB2", "db2"],
    "access": "Microsoft Access",
    "sqlite": "SQLite",
    "cassandra": "Cassandra",
    "snowflake": "Snowflake",
    "mariadb": "MariaDB",
    "dynamodb": ["DynamoDB", "Amazon DynamoDB"],
    "splunk": "Splunk",
    "firestore": ["Firestore", "Google Firestore"],
    "firebase-realtime-database": ["Firebase Realtime Database"],
    "neo4j": "Neo4j",
    "couchbase": "Couchbase",
    "hive": "Hive",
    "bigquery": ["BigQuery", "Google BigQuery"],
    "memcached": "Memcached",

}

web_frameworks = {
    "django": "Django",
    "flask": "Flask",
    "nodejs": "Node.js",
    "react": "React.js",
    "angular": "Angular",
    "jquery": "jQuery",
    "express": "Express",
    "vue": "Vue.js",
    "asp.net-core": "ASP.NET Core",
    "asp.net": "ASP.NET",
    "nextjs": "Next.js",
    "laravel": "Laravel",
    "angularjs": "Angular.js",
    "fastapi": "FastAPI",
    "ruby-on-rails": "Ruby on Rails",
    "svelte": "Svelte",
    "blazor": "Blazor",
    "nuxtjs": "Nuxt.js",
    "symfony": "Symfony",
    "gatsby": "Gatsby",

}

other_libraries = {
    "tensorflow": "Tensorflow",
    ".net": ".NET",
    "apache-kafka": "Apache Kafka",
    "spark": "Apache Spark",
    "cordova": "Cordova",
    "electro": "Electron",
    "flutter": "Flutter",
    "gtk": "GTK",
    "hadoop": "Hadoop",
    "ionic": "Ionic",
    "keras": "Keras",
    "numpy": "NumPy",
    "pandas": "Pandas",
    "qt": "Qt",
    "react-native": "React Native",
    "scikit-learn": "Scikit-learn",
    "spring": "Spring",
    "torch": "Torch/PyTorch",
    "xamarin": "Xamarin",
    "spring-boot": "Spring Boot",
    ".net-core": ".NET Core",
}

cloud_platforms = {
    "aws":"AWS",
    "digitalocean":"DigitalOcean",
    "firebase":"Firebase",
    "google-cloud":"Google Cloud",
    "heroku":"Heroku",
    "ibm":["IBM Cloud", "Watson", "IBM Watson"],
    "linode":"Linode",
    "managed":"Managed Hosting",
    "azure":"Microsoft Azure",
    "openstack":"OpenStack",
    "vmware":"VMware",
}

# devops = {}

# more info

lang_info = [
    {
        "type": "language",
        "language": "Python",
        "site": "https://www.python.org/",
        "docs": "https://docs.python.org/3/",
        "roadmap": "https://roadmap.sh/python",
        "awesome": "https://github.com/vinta/awesome-python"
    },
    {
        "type": "language",
        "language": "C++",
        "site": "",
        "docs": "https://learn.microsoft.com/en-us/cpp/cpp/?view=msvc-170",
        "roadmap": "",
        "awesome": "https://github.com/fffaraz/awesome-cpp"
    },
    {
        "type": "language",
        "language": "C",
        "site": "",
        "docs": "https://devdocs.io/c/",
        "roadmap": "",
        "awesome": "https://github.com/inputsh/awesome-c"
    },
    {
        "type": "language",
        "language": "JavaScript",
        "site": "",
        "docs": "https://developer.mozilla.org/en-US/docs/Web/javascript",
        "roadmap": "https://roadmap.sh/javascript",
        "awesome": "https://github.com/sorrycc/awesome-javascript"
    },
    {
        "type": "language",
        "language": "Java",
        "site": "https://www.java.com/en/",
        "docs": "https://docs.oracle.com/en/java/",
        "roadmap": "https://roadmap.sh/java",
        "awesome": "https://github.com/akullpp/awesome-java"
    },
    {
        "type": "language",
        "language": "PHP",
        "site": "https://www.php.net/",
        "docs": "https://www.php.net/docs.php",
        "roadmap": "",
        "awesome": "https://github.com/ziadoz/awesome-php"
    },
    {
        "type": "language",
        "language": "Rust",
        "site": "https://www.rust-lang.org/",
        "docs": "https://doc.rust-lang.org/",
        "roadmap": "",
        "awesome": "https://github.com/rust-unofficial/awesome-rust"
    },
    {
        "type": "language",
        "language": "Go",
        "site": "https://go.dev/",
        "docs": "https://go.dev/doc/",
        "roadmap": "https://roadmap.sh/golang",
        "awesome": "https://github.com/avelino/awesome-go"
    },
    {
        "type": "language",
        "language": "Dart",
        "site": "https://dart.dev/",
        "docs": "https://dart.dev/guides",
        "roadmap": "",
        "awesome": "https://github.com/yissachar/awesome-dart"
    },
    {
        "type": "language",
        "language": "Haskell",
        "site": "https://www.haskell.org/",
        "docs": "https://www.haskell.org/documentation/",
        "roadmap": "",
        "awesome": "https://github.com/krispo/awesome-haskell"
    },
    {
        "type": "language",
        "language": "Swift",
        "site": "https://www.swift.org/",
        "docs": "https://www.swift.org/documentation/",
        "roadmap": "",
        "awesome": "https://github.com/matteocrippa/awesome-swift"
    },
    {
        "type": "language",
        "language": "R",
        "site": "https://www.r-project.org",
        "docs": "https://cran.r-project.org/manuals.html",
        "roadmap": "",
        "awesome": "https://github.com/qinwf/awesome-R"
    },
    {
        "type": "language",
        "language": "Ruby",
        "site": "https://www.ruby-lang.org/en",
        "docs": "https://www.ruby-lang.org/en/documentation/",
        "roadmap": "",
        "awesome": "https://github.com/markets/awesome-ruby"
    },
    {
        "type": "language",
        "language": "Kotlin",
        "site": "https://kotlinlang.org",
        "docs": "https://kotlinlang.org/docs/home.html",
        "roadmap": "",
        "awesome": "https://github.com/KotlinBy/awesome-kotlin"
    },
    {
        "type": "language",
        "language": "HTML",
        "site": "",
        "docs": "https://developer.mozilla.org/en-US/docs/Web/HTML",
        "roadmap": "",
        "awesome": "https://github.com/diegocard/awesome-html5"
    },
    {
        "type": "language",
        "language": "CSS",
        "site": "",
        "docs": "https://developer.mozilla.org/en-US/docs/Web/CSS",
        "roadmap": "",
        "awesome": "https://github.com/awesome-css-group/awesome-css"
    },
    {
        "type": "language",
        "language": "TypeScript",
        "site": "https://www.typescriptlang.org",
        "docs": "https://www.typescriptlang.org/docs/",
        "roadmap": "",
        "awesome": "https://github.com/dzharii/awesome-typescript"
    },
    {
        "type": "language",
        "language": "Bash",
        "site": "https://www.gnu.org/software/bash/",
        "docs": "https://www.gnu.org/software/bash/manual/bash.html",
        "roadmap": "",
        "awesome": ""
    },
    {
        "type": "language",
        "language": "VBA",
        "site": "",
        "docs": "https://learn.microsoft.com/en-us/office/vba/api/overview/",
        "roadmap": "",
        "awesome": ""
    },
    {
        "type": "language",
        "language": "Scala",
        "site": "https://www.scala-lang.org",
        "docs": "https://docs.scala-lang.org/",
        "roadmap": "",
        "awesome": "https://github.com/lauris/awesome-scala"
    },
    {
        "type": "language",
        "language": "XML",
        "site": "",
        "docs": "https://developer.mozilla.org/en-US/docs/Web/XML/XML_introduction",
        "roadmap": "",
        "awesome": ""
    },
    {
        "type": "language",
        "language": "PowerShell",
        "site": "",
        "docs": "https://learn.microsoft.com/en-us/powershell/",
        "roadmap": "",
        "awesome": "https://github.com/janikvonrotz/awesome-powershell"
    },
    {
        "type": "language",
        "language": "MATLAB",
        "site": "https://www.mathworks.com/products/matlab.html",
        "docs": "https://www.mathworks.com/help/matlab/",
        "roadmap": "",
        "awesome": ""
    },
    {
        "type": "language",
        "language": "Lua",
        "site": "http://www.lua.org",
        "docs": "https://www.lua.org/manual/5.4/",
        "roadmap": "",
        "awesome": "https://github.com/LewisJEllis/awesome-lua"
    },
    {
        "type": "language",
        "language": "Groovy",
        "site": "http://groovy-lang.org/index.html",
        "docs": "http://groovy-lang.org/documentation.html",
        "roadmap": "",
        "awesome": "https://github.com/kdabir/awesome-groovy"
    },
    {
        "type": "language",
        "language": "Delphi",
        "site": "",
        "docs": "https://docwiki.embarcadero.com/RADStudio/Sydney/en/Delphi_Language_Reference",
        "roadmap": "",
        "awesome": ""
    },
    {
        "type": "language",
        "language": "Objective-C",
        "site": "",
        "docs": "https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html",
        "roadmap": "",
        "awesome": ""
    },
    {
        "type": "language",
        "language": "Perl",
        "site": "https://www.perl.org",
        "docs": "https://www.perl.org/docs.html",
        "roadmap": "",
        "awesome": "https://github.com/hachiojipm/awesome-perl"
    },
    {
        "type": "language",
        "language": "LISP",
        "site": "https://lisp-lang.org",
        "docs": "https://lisp-lang.org/learn/",
        "roadmap": "",
        "awesome": "https://github.com/CodyReichert/awesome-cl"
    },
    {
        "type": "language",
        "language": "Julia",
        "site": "https://julialang.org",
        "docs": "https://docs.julialang.org/en/v1/",
        "roadmap": "",
        "awesome": "https://github.com/svaksha/Julia.jl"
    }
]


def langList(indexed):
    li = list(lang_skills.values())
    # indexed = {}
    for i in range(len(li)):
        indexed[i] = li[i]

    return indexed

def dbList(indexed):
    li = list(db_skills.values())
    # indexed = {}
    for i in range(len(li)):
        if type(li[i]) is list:
            indexed[i+1] = li[i][0]
            pass
        else:
            indexed[i+1] = li[i]

    return indexed

def fullList(indexed):
    li = list(db_skills.values())
    li2 = list(lang_skills.values())
    # indexed = {}
    for i in range(len(li)):
        if type(li[i]) is list:
            indexed[i+1] = li[i][0]
            pass
        else:
            indexed[i+1] = li[i]

    for i in range(len(li), len(li)+len(li2)):
            j = i - len(li)
            indexed[i+1] = li2[j]

    return indexed

def skillInfo(skill):
    for i in lang_info:
        if i["language"] == skill:
            return i

# print(langList())



if __name__ == "__main__":
    skill = {}
    # i = langList(indexed)
    final = fullList(indexed)
    print(final)