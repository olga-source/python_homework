#Task#1: Diary
import traceback

try:
    with open('diary.txt', 'a') as file:
        prompt = "\nWhat happened today?\n"

        #infinite loop until we break it with "done for now"
        while True:
            answer = input(prompt)
            file.write(answer + "\n")

            if answer.lower() == "done for now":
                break

            prompt = "\nWhat else?\n" 

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"An exception occurred: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}") 