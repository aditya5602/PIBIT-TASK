import json

def convert_resume_to_json(txt_file, json_file):
    with open(txt_file, 'r') as file:
        lines = file.readlines()
    
    resume = {}
    current_section = None
    section_content = []

    def add_section_to_resume(section, content):
        if section:
            if section in ['Education', 'Experience', 'Projects', 'Certifications', 'Conferences and Workshops', 'Scholarships']:
                if section not in resume:
                    resume[section] = []
                resume[section].append("\n".join(content))
            else:
                resume[section] = "\n".join(content)

    for line in lines:
        line = line.strip()
        if line:
            if line in ['Summary', 'Education', 'Skills', 'Experience', 'Projects', 'Certifications', 'Conferences and Workshops', 'Scholarships', 'Links', 'Languages']:
                add_section_to_resume(current_section, section_content)
                current_section = line
                section_content = []
            else:
                section_content.append(line)
    
    add_section_to_resume(current_section, section_content)
    
    with open(json_file, 'w') as file:
        json.dump(resume, file, indent=4)

# Convert the resume.txt file to resume.json
convert_resume_to_json('resume.txt', 'resume.json')
