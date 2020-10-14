while true
do
curl -d '{"name":"Felipe", "email": "moz.felipe@gmail.com", "pwd":"$(RANDOM)"}' -H "Content-Type: application/json" -X POST http://127.0.0.1/add
done