cat planet.xml | curl -X POST -H 'Content-type: text/xml' -d @- http://127.0.0.1/xml2json