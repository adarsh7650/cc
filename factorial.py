#server.py
from flask import Flask , jsonify

app = Flask(__name__)

def fact(n):
    if(n==1):
        return n
    return n * fact(n-1)

@app.route("/fact/<int:num>" , methods=["GET"])
def facts_get(num):
    res = fact(num)
    return jsonify({"result" : res})
app.run()

#java
import java.net.URI;
import java.net.http.*;

public class CurrencyConverterClient{
    public static void main(String[] args) {
        HttpClient client = HttpClient.newHttpClient();
        String url = "http://localhost:5000/fact/4";
        HttpRequest request = HttpRequest.newBuilder().uri(URI.create(url)).build();

        client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
        .thenApply(HttpResponse::body)
        .thenAccept(System.out::println)
        .join();
    }
}