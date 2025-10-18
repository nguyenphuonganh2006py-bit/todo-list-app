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
