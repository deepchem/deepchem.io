import os


def template_file(header_lines, html_lines):
  html_lines = html_lines[85:]
  return header_lines + html_lines


def template_folder(folder, header_lines):
  html_files = os.listdir(folder)
  for f in html_files:
    if not f.endswith('html'):
      continue
    print(f)
    full_path = os.path.join(folder, f)
    if os.path.isfile(full_path):
      html_lines = open(full_path, encoding='UTF-8').readlines()
      templated_html = template_file(header_lines, html_lines)
      with open(full_path, 'w') as fout:
        new_html = "".join(templated_html)
        fout.write(new_html)


def template_131():
  header_lines = open("deepchemwebsite/1.3.1_header.html.j2").readlines()
  #template_folder('website/docs/2.0.0', header_lines)
  template_folder('website/docs/1.3.1', header_lines)


if __name__ == "__main__":
  template_131()
