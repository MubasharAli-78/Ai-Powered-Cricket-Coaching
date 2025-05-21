// import 'package:flutter/material.dart';
//
// import '../Manager/Coach.dart';
//
//
// class CoachScreen extends StatefulWidget {
//   const CoachScreen({super.key});
//
//   @override
//   State<CoachScreen> createState() => _CoachScreenState();
// }
//
// class _CoachScreenState extends State<CoachScreen> {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text(
//           "Coach",
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
//         decoration: BoxDecoration(
//           gradient: LinearGradient(
//             colors: [Colors.green.shade700, Colors.white],
//             begin: Alignment.topCenter,
//             end: Alignment.bottomCenter,
//           ),
//         ),
//         child: Center(
//           child: InkWell(
//             onTap: () {
//               Navigator.push(
//                 context,
//                 MaterialPageRoute(builder: (context) => const Coach()),
//               );
//             },
//             child: _builButton(Icons.person_outline, "Coach"),
//           ),
//         ),
//       ),
//     );
//   }
//
//   Widget _builButton(IconData icon, String text) {
//     return Container(
//       width: 280,
//       padding: const EdgeInsets.all(16),
//       decoration: BoxDecoration(
//         color: const Color(0xFFCED7CE),
//         borderRadius: BorderRadius.circular(8),
//         border: Border.all(color: const Color(0xFF1C3A6B)),
//       ),
//       child: Row(
//         mainAxisAlignment: MainAxisAlignment.center,
//         children: [
//           Expanded(
//             child: Column(
//               mainAxisSize: MainAxisSize.min,
//               children: [
//                 Icon(icon, size: 36, color: const Color(0xFF1C3A6B)),
//                 const SizedBox(height: 4),
//                 Text(
//                   text,
//                   style: const TextStyle(
//                     fontSize: 16,
//                     fontWeight: FontWeight.bold,
//                     color: Color(0xFF1C3A6B),
//                   ),
//                 ),
//               ],
//             ),
//           ),
//           const Icon(Icons.more_vert, color: Color(0xFF1C3A6B)),
//         ],
//       ),
//     );
//   }
// }