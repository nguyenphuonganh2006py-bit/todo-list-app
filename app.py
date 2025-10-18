# Danh sách lưu các công việc
tasks =[]
def add_task(task_name):
  """Thêm một công việc mới vào danh sách."""
  tasks.append(task_name)
  print(f"Đã thêm công việc:'{task_name}")
#---Điểm bắt đầu của chương trình---
if___name___=="__main__":
  print("Chào mừng đến với ứng dụng To-Do-List!")
  add_task("Học bài Git và GitHub")
  add_task("Làm bài tập thực hành ở nhà")
tasks = [] 
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name) 
    print(f"Đã thêm công việc: {task_name}")
def list_tasks():
    """Hàm sẽ duyệt qua danh sách tasks và in ra tất cả các công việc hiện có, theo định dạng có đánh số thứ tự."""
    if not tasks:
        print("Danh sách công việc trống.")
        return
    print("\n--- Danh sách công việc ---")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}") 
    print("--------------------------\n")
def delete_task(task_index):
    """Xóa công việc theo chỉ số."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"✅ Đã xóa công việc: {removed_task['name']}")
    else:
        print("❌ Không tồn tại công việc này!")

def update_task(index, new_name):
    """Cập nhật tên công việc."""
    if 0 <= index < len(tasks):
        old_name = tasks[index]["name"]
        tasks[index]["name"] = new_name
        print(f"✏️ Đã cập nhật: '{old_name}' → '{new_name}'")
    else:
        print("❌ Không tìm thấy công việc cần cập nhật.")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    complete_task(0)
    list_tasks()
    delete_task(1)
    update_task(0, "Ôn lại Git cơ bản")
    list_tasks()