# 2024_programming-challenges-1
Programming challenges for internship applicants - 1

โจทย์ 1 : การหาค่าผสมที่เป็นไปได้ของเลขชุดที่ให้ผลรวมเป็นจำนวนเฉพาะ
**รายละเอียด:** เขียนโปรแกรมที่รับอาร์เรย์ของจำนวนเต็มและจำนวนเต็มหนึ่งจำนวน (ผลรวมที่ต้องการ) แล้วทำการหาค่าผสมของตัวเลขในอาร์เรย์ที่มีผลรวมเป็นจำนวนเฉพาะ
- **อินพุต:** อาร์เรย์ของจำนวนเต็ม และจำนวนเต็มหนึ่งจำนวน
- **เอาท์พุต:** ลิสต์ของค่าผสมที่ผลรวมเป็นจำนวนเฉพาะ

**ตัวอย่าง:**
- อินพุต: [2, 3, 5, 7, 11], 10
- เอาท์พุต: [[3, 7], [5, 5]]


### โจทย์ 2 : การหาคำที่ใช้ตัวอักษรทุกตัวในภาษาอังกฤษอย่างน้อยหนึ่งครั้ง (Pangram)
**รายละเอียด:** เขียนโปรแกรมที่รับสตริงหนึ่งสตริงแล้วตรวจสอบว่าสตริงนั้นเป็น Pangram หรือไม่ ถ้าใช่ ให้หาคำที่ยาวที่สุดในสตริงนั้น
- **อินพุต:** สตริงหนึ่งสตริง
- **เอาท์พุต:** สตริงที่เป็นคำยาวที่สุดในสตริงที่เป็น Pangram หรือข้อความแสดงว่าไม่ใช่ Pangram

**ตัวอย่าง:**
- อินพุต: "The quick brown fox jumps over the lazy dog"
- เอาท์พุต: "jumps"
- อินพุต: "Hello world"
- เอาท์พุต: "Not a Pangram"


### โจทย์ 3 : การหาทางเดินที่สั้นที่สุดในกราฟ (Shortest Path in Graph)
**รายละเอียด:** เขียนโปรแกรมที่รับกราฟที่เป็นการเชื่อมต่อระหว่างจุดต่างๆ และหาทางเดินที่สั้นที่สุดระหว่างจุดเริ่มต้นและจุดสิ้นสุดโดยใช้ Dijkstra's Algorithm
- **อินพุต:** กราฟที่เป็นลิสต์ของคู่จุดเชื่อมต่อ (edges) และน้ำหนัก (weight) ของการเชื่อมต่อแต่ละคู่ จุดเริ่มต้นและจุดสิ้นสุด
- **เอาท์พุต:** ความยาวของทางเดินที่สั้นที่สุด

**ตัวอย่าง:**
- อินพุต: [(1, 2, 1), (2, 3, 2), (1, 3, 4), (3, 4, 1)], จุดเริ่มต้น: 1, จุดสิ้นสุด: 4
- เอาท์พุต: 4


## วิธีการส่งงาน
1. Fork repository นี้ไปยังบัญชี GitHub ของคุณ
2. Clone repository ที่คุณ fork มา
3. สร้างโฟลเดอร์ใหม่ใน `submissions` โดยใช้ชื่อ GitHub ของคุณ
4. เขียนโปรแกรมแก้โจทย์ทั้ง 3 ข้อในโฟลเดอร์ที่สร้างขึ้นมาใหม่ โดยเลือกใช้ภาษา C# ,Java ,Python 1 ใน 3 ภาษานี้ 
5. Commit และ push โค้ดของคุณไปยัง repository ที่คุณ fork มา
6. เปิด Pubilc Repo ของคุณ และแจ้งกลับมายังบริษัท
