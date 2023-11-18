from scenario1 import create_palindrome_frame
from window import ApplicationWindow

app = ApplicationWindow(create_palindrome_frame)
app.set_title('Window Skeleton')
app.mainloop()
