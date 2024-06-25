import sys
import os 
import comtypes.client

input_folder_path = r"C:\Users\wbc21\Downloads\CH 5. Network Layer - Control Plane (2).pptx"
output_folder_path = r"C:\Users\wbc21\Downloads"
input_file_paths = os.listdir(input_folder_path)


for input_file_name in input_file_paths:

    if not input_file_name.lower().endswith((".ppt", ".pptx")):
        continue
    
    input_file_path = os.path.join(input_folder_path, input_file_name)
        
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = True
    slides = powerpoint.Presentations.Open(input_file_path)
    
    file_name = os.path.splitext(input_file_name)[0]
    output_file_path = os.path.join(output_folder_path, file_name + ".pdf")
    
    slides.SaveAs(output_file_path, FileFormat=32)
    slides.Close()
