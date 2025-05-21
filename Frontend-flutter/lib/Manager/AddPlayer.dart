// import 'package:flutter/material.dart';
//
// class AddPlayer extends StatefulWidget {
//   const AddPlayer({super.key});
//
//   @override
//   State<AddPlayer> createState() => _AddPlayerState();
// }
//
// class _AddPlayerState extends State<AddPlayer> {
//   // Dropdown options for the "Type" field
//   final List<String> _typeOptions = ["Right HandBatsman", "Left HandBatsman"];
//
//   // Currently selected option
//   String? _selectedType;
//
//   @override
//   void initState() {
//     super.initState();
//     // Initialize the dropdown with the first item (if available)
//     _selectedType = _typeOptions.isNotEmpty ? _typeOptions[0] : null;
//   }
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text(
//           "Add Player",
//           style: TextStyle(color: Color(0xFF1C3A6B)),
//         ),
//         backgroundColor: const Color(0xFFCED7CE),
//         centerTitle: true,
//         leading: IconButton(
//           icon: const Icon(Icons.arrow_back, color: Colors.black),
//           onPressed: () => Navigator.pop(context),
//         ),
//       ),
//       body: Container(
//         // Green-to-white gradient background
//         decoration: BoxDecoration(
//           gradient: LinearGradient(
//             colors: [Colors.green.shade700, Colors.white],
//             begin: Alignment.topCenter,
//             end: Alignment.bottomCenter,
//           ),
//         ),
//         // Centers content on the screen
//         child: Center(
//           // Makes content scrollable if screen is too small
//           child: SingleChildScrollView(
//             child: SizedBox(
//               width: 300, // Constrain form width
//               child: Column(
//                 crossAxisAlignment: CrossAxisAlignment.start,
//                 children: [
//                   // NAME
//                   const Text("Name"),
//                   const SizedBox(height: 10),
//                   _buildTextField("Name"),
//                   const SizedBox(height: 20),
//
//                   // AGE
//                   const Text("Age"),
//                   const SizedBox(height: 10),
//                   _buildTextField("Age"),
//                   const SizedBox(height: 20),
//
//                   // EXPERIENCE
//                   const Text("Experience"),
//                   const SizedBox(height: 10),
//                   _buildTextField("Experience"),
//                   const SizedBox(height: 20),
//
//                   // CONTACT NUMBER
//                   const Text("Contact Number"),
//                   const SizedBox(height: 10),
//                   _buildTextField("Contact Number"),
//                   const SizedBox(height: 20),
//
//                   // TYPE (DROPDOWN)
//                   const Text("Type"),
//                   const SizedBox(height: 10),
//                   _buildDropdown(),
//                   const SizedBox(height: 20),
//
//                   // USERNAME
//                   const Text("Username"),
//                   const SizedBox(height: 10),
//                   _buildTextField("Username"),
//                   const SizedBox(height: 20),
//
//                   // PASSWORD
//                   const Text("Password"),
//                   const SizedBox(height: 10),
//                   _buildTextField("Password"),
//                   const SizedBox(height: 30),
//
//                   // SAVE BUTTON
//                   SizedBox(
//                     width: double.infinity,
//                     child: ElevatedButton(
//                       style: ElevatedButton.styleFrom(
//                         backgroundColor: Colors.green.shade700,
//                         shape: RoundedRectangleBorder(
//                           borderRadius: BorderRadius.circular(10),
//                         ),
//                         padding: const EdgeInsets.symmetric(vertical: 16),
//                       ),
//                       onPressed: () {
//                         // Handle save action
//                       },
//                       child: const Text(
//                         "Save",
//                         style: TextStyle(fontSize: 18, color: Colors.white),
//                       ),
//                     ),
//                   ),
//                   const SizedBox(height: 15),
//
//                   // CANCEL BUTTON
//                   SizedBox(
//                     width: double.infinity,
//                     child: ElevatedButton(
//                       style: ElevatedButton.styleFrom(
//                         backgroundColor: Colors.green.shade700,
//                         shape: RoundedRectangleBorder(
//                           borderRadius: BorderRadius.circular(10),
//                         ),
//                         padding: const EdgeInsets.symmetric(vertical: 16),
//                       ),
//                       onPressed: () {
//                         // Handle cancel action
//                       },
//                       child: const Text(
//                         "Cancel",
//                         style: TextStyle(fontSize: 18, color: Colors.white),
//                       ),
//                     ),
//                   ),
//                   const SizedBox(height: 30),
//                 ],
//               ),
//             ),
//           ),
//         ),
//       ),
//     );
//   }
//
//   // Reusable text field builder with matching style
//   Widget _buildTextField(String labelText) {
//     return TextFormField(
//       decoration: InputDecoration(
//         labelText: labelText,
//         labelStyle: const TextStyle(color: Color(0xFF1C3A6B)),
//         enabledBorder: OutlineInputBorder(
//           borderRadius: BorderRadius.circular(10),
//           borderSide: const BorderSide(color: Color(0xFF1C3A6B)),
//         ),
//         focusedBorder: OutlineInputBorder(
//           borderRadius: BorderRadius.circular(10),
//           borderSide: const BorderSide(color: Color(0xFF1C3A6B), width: 2),
//         ),
//       ),
//     );
//   }
//
//   // Dropdown for "Type" with same border style
//   Widget _buildDropdown() {
//     return DropdownButtonFormField<String>(
//       value: _selectedType,
//       decoration: InputDecoration(
//         enabledBorder: OutlineInputBorder(
//           borderRadius: BorderRadius.circular(10),
//           borderSide: const BorderSide(color: Color(0xFF1C3A6B)),
//         ),
//         focusedBorder: OutlineInputBorder(
//           borderRadius: BorderRadius.circular(10),
//           borderSide: const BorderSide(color: Color(0xFF1C3A6B), width: 2),
//         ),
//       ),
//       items: _typeOptions.map((String type) {
//         return DropdownMenuItem<String>(
//           value: type,
//           child: Text(
//             type,
//             style: const TextStyle(color: Color(0xFF1C3A6B)),
//           ),
//         );
//       }).toList(),
//       onChanged: (newValue) {
//         setState(() {
//           _selectedType = newValue;
//         });
//       },
//     );
//   }
// }



import 'package:flutter/material.dart';

class AddPlayer extends StatefulWidget {
  const AddPlayer({super.key});

  @override
  State<AddPlayer> createState() => _AddPlayerState();
}

class _AddPlayerState extends State<AddPlayer> {
  final List<String> _typeOptions = ["Right HandBatsman", "Left HandBatsman"];
  String? _selectedType;

  @override
  void initState() {
    super.initState();
    _selectedType = _typeOptions.isNotEmpty ? _typeOptions[0] : null;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "Add Player",
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
          child: SingleChildScrollView(
            child: SizedBox(
              width: 300,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text("Name"),
                  const SizedBox(height: 10),
                  _buildTextField("Name"),
                  const SizedBox(height: 20),
                  const Text("Age"),
                  const SizedBox(height: 10),
                  _buildTextField("Age"),
                  const SizedBox(height: 20),
                  const Text("Experience"),
                  const SizedBox(height: 10),
                  _buildTextField("Experience"),
                  const SizedBox(height: 20),
                  const Text("Contact Number"),
                  const SizedBox(height: 10),
                  _buildTextField("Contact Number"),
                  const SizedBox(height: 20),
                  const Text("Type"),
                  const SizedBox(height: 10),
                  _buildDropdown(),
                  const SizedBox(height: 20),
                  const Text("Username"),
                  const SizedBox(height: 10),
                  _buildTextField("Username"),
                  const SizedBox(height: 20),
                  const Text("Password"),
                  const SizedBox(height: 10),
                  _buildTextField("Password"),
                  const SizedBox(height: 30),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.green.shade700,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10),
                        ),
                        padding: const EdgeInsets.symmetric(vertical: 16),
                      ),
                      onPressed: () {
                        // Handle save action
                      },
                      child: const Text(
                        "Save",
                        style: TextStyle(fontSize: 18, color: Colors.white),
                      ),
                    ),
                  ),
                  const SizedBox(height: 15),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.green.shade700,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10),
                        ),
                        padding: const EdgeInsets.symmetric(vertical: 16),
                      ),
                      onPressed: () {
                        // Handle cancel action
                      },
                      child: const Text(
                        "Cancel",
                        style: TextStyle(fontSize: 18, color: Colors.white),
                      ),
                    ),
                  ),
                  const SizedBox(height: 30),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildTextField(String labelText) {
    return TextFormField(
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
    );
  }

  Widget _buildDropdown() {
    return DropdownButtonFormField<String>(
      value: _selectedType,
      decoration: InputDecoration(
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
          borderSide: const BorderSide(color: Color(0xFF1C3A6B)),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
          borderSide: const BorderSide(color: Color(0xFF1C3A6B), width: 2),
        ),
      ),
      items: _typeOptions.map((String type) {
        return DropdownMenuItem<String>(
          value: type,
          child: Text(
            type,
            style: const TextStyle(color: Color(0xFF1C3A6B)),
          ),
        );
      }).toList(),
      onChanged: (newValue) {
        setState(() {
          _selectedType = newValue;
        });
      },
    );
  }
}
