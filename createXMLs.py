import os

def create_xml_for_wav(wav_folder, template_xml_path, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all .wav files in the specified folder
    for wav_file in os.listdir(wav_folder):
        if wav_file.endswith('.wav'):
            # Read the template XML content
            with open(template_xml_path, 'r') as file:
                xml_content = file.read()

            # Replace the line with the new content, including the .wav file name
            new_line = f'fileName="SAMPLES/WAVETABLES/OsirisWavetables/{wav_file}" />'
            xml_content = xml_content.replace('fileName="SAMPLES/WAVETABLES/CommunityWavetables/Basic Shapes.wav', new_line)

            # Define the output XML file path
            output_xml_path = os.path.join(output_folder, os.path.splitext(wav_file)[0] + '.xml')

            # Write the modified XML content to the new file
            with open(output_xml_path, 'w') as file:
                file.write(xml_content)

# Example usage
wav_folder = '.'  # Change this to your .wav files folder
template_xml_path = './template.xml'  # Change this to your template XML file path
output_folder = './OsirisWavetables'  # Change this to your desired output folder path

create_xml_for_wav(wav_folder, template_xml_path, output_folder)
