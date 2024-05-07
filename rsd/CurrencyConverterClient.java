import java.net.URI;
import java.net.http.*;

public class CurrencyConverterClient {
    public static void main(String[] args) {
        
        HttpClient client = HttpClient.newHttpClient();
        String url = "http://localhost:5000/convert?amount=100";
        HttpRequest request = HttpRequest.newBuilder().uri(URI.create(url)).build();

        client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
              .thenApply(HttpResponse::body)
              .thenAccept(System.out::println)
              .join(); 
    }
}
