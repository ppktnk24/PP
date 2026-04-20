def manage_shopping_list():
    # สร้าง Dictionary ว่างสำหรับเก็บรายการ
    shopping_list = {}

    while True:
        print("\n" + "="*35)
        print("🛒 ระบบจัดการรายการซื้อวัตถุดิบ 🛒")
        print("="*35)
        print("1. เพิ่มวัตถุดิบ / แก้ไขจำนวน")
        print("2. ดูรายการที่ต้องซื้อทั้งหมด")
        print("3. ลบวัตถุดิบออกจากรายการ")
        print("4. ออกจากโปรแกรม")
        print("="*35)
        
        choice = input("กรุณาเลือกเมนู (1-4): ")

        if choice == '1':
            item = input("👉 ใส่ชื่อวัตถุดิบที่ต้องการซื้อ: ").strip()
            if not item:
                print("⚠️ กรุณาใส่ชื่อวัตถุดิบ!")
                continue
                
            quantity = input("👉 ใส่จำนวน (เช่น 2 กก., 3 ขวด, 10 ชิ้น): ").strip()
            
            # เก็บข้อมูลลงใน Dictionary
            shopping_list[item] = quantity
            print(f"✅ เพิ่ม/อัปเดต '{item}' จำนวน '{quantity}' เรียบร้อยแล้ว!")

        elif choice == '2':
            if not shopping_list:
                print("\n📭 ตอนนี้ยังไม่มีรายการในลิสต์")
            else:
                print("\n📋 รายการที่คุณต้องซื้อ:")
                # วนลูปเพื่อแสดงรายการทั้งหมด
                for index, (item, qty) in enumerate(shopping_list.items(), start=1):
                    print(f"  {index}. {item} - {qty}")

        elif choice == '3':
            item = input("🗑️ ใส่ชื่อวัตถุดิบที่ต้องการลบ: ").strip()
            if item in shopping_list:
                del shopping_list[item]
                print(f"✅ ลบ '{item}' ออกจากรายการเรียบร้อยแล้ว!")
            else:
                print(f"❌ ไม่พบ '{item}' ในรายการของคุณ")

        elif choice == '4':
            print("\n👋 ปิดโปรแกรม ขอให้สนุกกับการช้อปปิ้งครับ!\n")
            break  # ออกจากลูป while เพื่อจบโปรแกรม

        else:
            print("⚠️ กรุณาเลือกตัวเลขเมนูให้ถูกต้อง (1-4)")

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    manage_shopping_list()