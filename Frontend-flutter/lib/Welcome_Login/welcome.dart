
import 'package:flutter/material.dart';

import 'login.dart';

class welcome extends StatelessWidget {
  const welcome({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //This is only for backgroundColor colors
      body: Container(
        decoration: BoxDecoration(
            gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors:[Colors.green.shade700,Colors.white]
            )
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            SizedBox(height: 50),
            Padding(padding:
            EdgeInsets.symmetric(horizontal: 20.0),
              child: Column(
                children: [
                  Text("Welcome to Cricket Coach",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                      color: Colors.blue.shade900,
                    ),
                    textAlign: TextAlign.center,),
                  SizedBox(height: 5),
                  Text("AI Powered Cricket Coaching",
                    style: TextStyle(
                      fontSize: 16,
                      color: Colors.black54,
                    ),
                    textAlign: TextAlign.center,)



                ],
              ),),
            SizedBox(height: 40),
            Image.asset(
                "assets/image/logo.png"
            ),
            SizedBox(height: 50),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green.shade700,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(20),
                ),
                padding: const EdgeInsets.symmetric(horizontal: 50, vertical: 12),
              ),
              onPressed: (){
                Navigator.push(context,
                    MaterialPageRoute(builder: (context)=>loginScrren()));

              } ,  child: Text(
              "Sign In",
              style: TextStyle(fontSize: 18, color: Colors.white),
            ),

            )

          ],
        ),
      ),

    );
  }
}