# Danh sách để lưu các công việc dưới dạng dictionary
tasks = []

def add_task(task_name):
    """Thêm một công việc mới với trạng thái chưa hoàn thành."""
    task_dict = {"name": task_name, "completed": False}
    tasks.append(task_dict)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """Duyệt qua danh sách tasks và in ra kèm trạng thái [x] hoặc [ ]."""
    if not tasks:
        print("Danh sách công việc trống!")
    else:
        print("Danh sách công việc:")
        for index, task in enumerate(tasks, start=1):
            status = "x" if task["completed"] else " "
            print(f"{index}. [{status}] {task['name']}")

def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành dựa vào chỉ số (index)."""
    real_index = task_index - 1
    if 0 <= real_index < len(tasks):
        tasks[real_index]["completed"] = True
        print(f"Đã đánh dấu hoàn thành: '{tasks[real_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    
    # Đánh dấu công việc đầu tiên hoàn thành
    complete_task(1)
    
    # Hiển thị lại danh sách
    list_tasks()