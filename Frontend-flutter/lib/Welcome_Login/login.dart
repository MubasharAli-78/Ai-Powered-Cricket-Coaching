import 'dart:convert';
import 'package:flutter/material.dart';
import '../Manager/Coach.dart';
import '../Manager/ManagerDashboard.dart';
import '../Player/PlayerDashboard.dart';

import '../Backend/Connectivity.dart'; // Adjust the path if needed

class loginScrren extends StatefulWidget {
  const loginScrren({super.key});

  @override
  State<loginScrren> createState() => _loginScrrenState();
}

class _loginScrrenState extends State<loginScrren> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  // Function to perform sign in by calling the backend using ConnectivityService.
  Future<void> _signIn() async {
    try {
      final response = await ConnectivityService.post('/login', {
        "username": _usernameController.text,
        "password": _passwordController.text,
      });

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        if (data["value"] == true) {
          final role = data["role"];
          // Navigate based on the role from backend.
          if (role == "manager") {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => ManagerScreen()),
            );
          } else if (role == "coach") {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => CoachScreen()),
            );
          } else if (role == "player") {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => PlayerScreen()),
            );
          } else {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text("Invalid role returned from server.")),
            );
          }
        } else {
          // Display backend error message.
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text(data["message"] ?? "Login failed")),
          );
        }
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Server error: ${response.statusCode}")),
        );
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text("An error occurred: $e")),
      );
    }
  }

  @override
  void dispose() {
    _usernameController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Colors.green.shade700, Colors.white],
          ),
        ),
        child: Column(
          children: [
            // Back Button at Top-Left
            Align(
              alignment: Alignment.topLeft,
              child: Padding(
                padding: EdgeInsets.only(left: 10, top: 40),
                child: IconButton(
                  icon: Icon(Icons.arrow_back, color: Colors.black),
                  onPressed: () {
                    Navigator.pop(context);
                  },
                ),
              ),
            ),
            // Main Content wrapped with Expanded & SingleChildScrollView
            Expanded(
              child: SingleChildScrollView(
                child: Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Image.asset(
                        'assets/image/logo.png',
                        height: 200,
                        width: 200,
                        fit: BoxFit.cover,
                      ),
                      SizedBox(height: 10),
                      Text(
                        "Sign In",
                        style: TextStyle(
                          fontSize: 22,
                          fontWeight: FontWeight.bold,
                          color: Colors.blue.shade900,
                        ),
                        textAlign: TextAlign.center,
                      ),
                      SizedBox(height: 20),
                      SizedBox(
                        width: 300,
                        child: TextFormField(
                          controller: _usernameController,
                          decoration: InputDecoration(
                            labelText: "Username",
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(10),
                            ),
                            prefixIcon: Icon(Icons.person, color: Colors.black),
                            contentPadding: EdgeInsets.symmetric(vertical: 15),
                          ),
                        ),
                      ),
                      SizedBox(height: 20),
                      SizedBox(
                        width: 300,
                        child: TextFormField(
                          controller: _passwordController,
                          obscureText: true,
                          decoration: InputDecoration(
                            labelText: "Password",
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(10),
                            ),
                            prefixIcon: Icon(Icons.lock, color: Colors.black),
                            contentPadding: EdgeInsets.symmetric(vertical: 15),
                          ),
                        ),
                      ),
                      SizedBox(height: 40),
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.green.shade700,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(20),
                          ),
                          padding: const EdgeInsets.symmetric(
                              horizontal: 50, vertical: 12),
                        ),
                        onPressed: _signIn,
                        child: Text(
                          "Sign In",
                          style: TextStyle(fontSize: 18, color: Colors.white),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}