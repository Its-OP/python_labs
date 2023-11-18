from scenario1 import set_palindrome_frame
from scenario2 import set_equation_frame
from scenario3 import set_sentence_frame
from window import ApplicationWindow

# Scenario 1
# app = ApplicationWindow(set_palindrome_frame)
# app.set_title('Palindromes')

# Scenario 2
# app = ApplicationWindow(set_equation_frame)
# app.set_title('Equations')

# Scenario 3
app = ApplicationWindow(set_sentence_frame)
app.set_title('Sentences')
app.mainloop()
