import 'dart:convert';
import 'package:http/http.dart' as http;

class ConnectivityService {
  /// Base URL for your backend.
  /// Change the IP address and port according to your backend settings.
  static const String baseUrl = "http://192.168.10.8:5000";

  /// Default headers for HTTP requests.
  static const Map<String, String> headers = {
    "Content-Type": "application/json",
  };

  /// Generic method for POST requests.
  /// [endpoint] is the API path (e.g., '/login').
  /// [body] is a Map of the JSON data to be sent.
  static Future<http.Response> post(
    String endpoint,
    Map<String, dynamic> body,
  ) async {
    final Uri url = Uri.parse('$baseUrl$endpoint');
    try {
      final response = await http.post(
        url,
        headers: headers,
        body: jsonEncode(body),
      );
      return response;
    } catch (error) {
      throw Exception("POST request error: $error");
    }
  }

  /// Generic method for GET requests.
  /// [endpoint] is the API path to fetch data from.
  static Future<http.Response> get(String endpoint) async {
    final Uri url = Uri.parse('$baseUrl$endpoint');
    try {
      final response = await http.get(url, headers: headers);
      return response;
    } catch (error) {
      throw Exception("GET request error: $error");
    }
  }
}
