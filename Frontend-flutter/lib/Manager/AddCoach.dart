import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';

class Addcoach extends StatefulWidget {
  const Addcoach({super.key});

  @override
  State<Addcoach> createState() => _AddcoachState();
}

class _AddcoachState extends State<Addcoach> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _ageController = TextEditingController();
  final TextEditingController _experienceController = TextEditingController();
  final TextEditingController _contactController = TextEditingController();
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  File? _selectedImage;

  void _saveCoach() {
    // Implement your save logic here
    print("Coach Saved");
  }

  void _upload() async {
    final ImagePicker picker = ImagePicker();
    final XFile? image = await picker.pickImage(source: ImageSource.gallery);

    if (image != null) {
      setState(() {
        _selectedImage = File(image.path);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Add Coach", style: TextStyle(color: Color(0xFF1C3A6B))),
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
          child: SingleChildScrollView(
            child: SizedBox(
              width: 300,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  _buildFormField("Name", _nameController),
                  _buildFormField("Age", _ageController),
                  _buildFormField("Experience", _experienceController),
                  _buildFormField("Contact Number", _contactController),
                  _buildFormField("Username", _usernameController),
                  _buildFormField("Password", _passwordController),
                  const SizedBox(height: 20),

                  // Display selected image above the upload button
                  if (_selectedImage != null)
                    CircleAvatar(
                      radius: 50,
                      backgroundImage: FileImage(_selectedImage!),
                    ),

                  const SizedBox(height: 20),

                  _buildActionButton("Upload", _upload),
                  const SizedBox(height: 15),
                  _buildActionButton("Save", _saveCoach),
                  const SizedBox(height: 15),
                  _buildActionButton("Cancel", () => Navigator.pop(context)),
                  const SizedBox(height: 30),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildFormField(String labelText, TextEditingController controller) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(labelText, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
        const SizedBox(height: 10),
        TextFormField(
          controller: controller,
          decoration: InputDecoration(
            labelText: labelText,
            labelStyle: const TextStyle(color: Color(0xFF1C3A6B)),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: const BorderSide(color: Color(0xFF1C3A6B)),
            ),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: const BorderSide(color: Color(0xFF1C3A6B), width: 2),
            ),
          ),
        ),
        const SizedBox(height: 20),
      ],
    );
  }

  Widget _buildActionButton(String text, VoidCallback onPressed) {
    return SizedBox(
      width: double.infinity,
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.green.shade700,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(10),
          ),
          padding: const EdgeInsets.symmetric(vertical: 16),
        ),
        onPressed: onPressed,
        child: Text(
          text,
          style: const TextStyle(fontSize: 18, color: Colors.white),
        ),
      ),
    );
  }
}
