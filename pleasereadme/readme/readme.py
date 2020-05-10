from collections import OrderedDict


class CustomReadme:
    """docstring for CustomReadme."""

    def __init__(self, title=None, description=None, sections=None) -> str:
        self.title = title or "Title"
        self.description = description or ""
        unordered_secs = sections or {}

        self.sections = OrderedDict(unordered_secs)


    def generate_template(self):
        template = f"# {self.title}"

        if self.description != "":
            template += f"\n{self.description}"

        for section_names, section_data in self.sections.items():
            template += f"\n\n## {section_names}"

            section_data = OrderedDict(section_data)

            for part_id, part_data in section_data.items():
                option = part_data[0]

                if option == "title":
                    template += f"\n### {part_data[1]}"
                elif option == "sub-title":
                    template += f"\n#### {part_data[1]}"
                elif option == "code":
                    template += f"\n```{part_data[1]}```"
                elif option == "multi-line-code":
                    template += f"\n\n```{part_data[2]}"
                    for code_line in part_data[1]:
                        template += f"\n{code_line}"
                    template += f"\n```"
                elif option == "text":
                    template += f"\n{part_data[1]}"
                elif option == "blockquote":
                    template += f"\n> {part_data[1]}"
                elif option == "multi-line-blockquote":
                    for line in part_data[1]:
                        template += f"\n > {line}"
                elif option == "hr":
                    template += "\n***"
                elif option == "ul":
                    for item in part_data[1]:
                        template += f"\n* {item}"
                elif option == "ol":
                    for enumeration_tuple in enumerate(part_data[1]):
                        template += (
                            f"\n{enumeration_tuple[0]+1}. {enumeration_tuple[1]}"
                        )
                else:
                    template += f"\n {part_data[1]}"

        return template


    def create(self, path=None) -> str:
        path = path or "README.md"
        template = self.generate_template()

        readme = open(path, "w+")
        readme.write(template)
        readme.close()

        return template
