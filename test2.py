line = '"ប៉ុន្តែនោះធ្វើឱ្យតួនាទីរបស់ឪពុកម្តាយគ្រាន់តែធ្វើឱ្យមានការភ័ន្តច្រឡំជាងមុន។"'
model_name = "source"
command = ["echo", line , "|", "spm_encode",
            f"--model={model_name}.model"]
print (" ".join(command))
import subprocess            
# Running the subprocess with the provided command
result = subprocess.run(command, capture_output=True, text=True)
print ("*********************************")
# Print the result of the subprocess
print(result.stdout)
