import 'package:flutter/material.dart';

class ManagerScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "Manager Dashboard",
          style: TextStyle(color: Color(0xFF1C3A6B)),
        ),
        backgroundColor: const Color(0xFFCED7CE),
        centerTitle: true,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back, color: Colors.black),
          onPressed: () => Navigator.pop(context),
        ),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.green.shade700, Colors.white],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              _buildButton(Icons.person, "Manager"),
              const SizedBox(height: 20),
              _buildButton(Icons.person_outline, "Coach"),
              const SizedBox(height: 20),
              _buildButton(Icons.groups_outlined, "Team"),
              const SizedBox(height: 20),
              _buildButton(Icons.person, "Player"),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildButton(IconData icon, String text) {
    return Container(
      width: 280,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFFCED7CE),
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: const Color(0xFF1C3A6B)),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(
            child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(icon, size: 36, color: const Color(0xFF1C3A6B)),
                  const SizedBox(height: 4),
                  Text(text,
                      style: const TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                        color: Color(0xFF1C3A6B),
                      )),
                ]),
          ),
          const Icon(Icons.more_vert, color: Color(0xFF1C3A6B)),
        ],
      ),
    );
  }
}