import 'package:flutter/material.dart';

class CoachScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
        title: Text("Coach", style: TextStyle(fontWeight: FontWeight.bold)),
        backgroundColor: Colors.grey[300],
        centerTitle: true,
      ),
      body: Container(padding: EdgeInsets.symmetric(horizontal: 16), // Apply padding to screen
    decoration: BoxDecoration(
    gradient: LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors:[Colors.green.shade700,Colors.white]
    )
    ),
        child: Column(
          children: [
            Spacer(), // Push content to center

            // Coach Box
            Container(
              padding: EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: Colors.green[300],
                borderRadius: BorderRadius.circular(10),
                border: Border.all(color: Colors.black),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      Icon(Icons.person, color: Colors.blue, size: 40),
                      SizedBox(width: 10),
                      Text("Coach", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                    ],
                  ),
                  Icon(Icons.more_vert, color: Colors.black),
                ],
              ),
            ),

            SizedBox(height: 30), // Space between Coach Box and Buttons

            // Add & View Coach Buttons
            Container(
              padding: EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Column(
                children: [
                  // Add Coach Button
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.green[300],
                      padding: EdgeInsets.symmetric(vertical: 15),
                    ),
                    onPressed: () {},
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.person_add, color: Colors.blue),
                        SizedBox(width: 8),
                        Text("Add Coach", style: TextStyle(fontSize: 16, color: Colors.black)),
                      ],
                    ),
                  ),

                  SizedBox(height: 20), // Space between buttons

                  // View Coaches Button
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.green[300],
                      padding: EdgeInsets.symmetric(vertical: 15),
                    ),
                    onPressed: () {},
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.groups, color: Colors.blue),
                        SizedBox(width: 8),
                        Text("View Coaches", style: TextStyle(fontSize: 16, color: Colors.black)),
                      ],
                    ),
                  ),
                ],
              ),
            ),

            Spacer(), // Push content to center
          ],
        ),
      ),
    );
  }
}
