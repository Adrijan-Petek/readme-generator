#!/usr/bin/env python3
"""
Universal README Generator
A CLI tool to generate professional README files for projects.
"""

import argparse
import os
import sys
import json
from git import Repo
from jinja2 import Template

def get_user_input():
    print("🚀 Let's create a beautiful README for your project!")
    print("=" * 50)
    
    name = input("📝 Project name (My Project): ").strip() or "My Project"
    description = input("📖 Project description: ").strip()
    author = input("👤 Author name: ").strip()
    email = input("📧 Author email: ").strip()
    
    # License options
    license_choice = input("📄 License (MIT/APACHE/GPL/NONE): ").strip().upper()
    if license_choice not in ['MIT', 'APACHE', 'GPL', 'NONE']:
        license_choice = 'MIT'
    
    # Social media links
    print("\n🌐 Social Media Links (leave empty to skip):")
    twitter = input("🐦 Twitter/X handle: ").strip()
    farcaster = input("🎭 Farcaster username: ").strip()
    zora = input("🎨 Zora profile: ").strip()
    website = input("🌍 Website URL: ").strip()
    linkedin = input("💼 LinkedIn profile: ").strip()
    github = input("🐙 GitHub username: ").strip()
    
    # Features to include
    include_badges = input("🏷️  Include badges? (y/n): ").strip().lower() == 'y'
    include_social = input("🔗 Include social links? (y/n): ").strip().lower() == 'y'
    include_install = input("📦 Include installation instructions? (y/n): ").strip().lower() == 'y'
    include_usage = input("💡 Include usage examples? (y/n): ").strip().lower() == 'y'
    include_contributing = input("🤝 Include contributing guide? (y/n): ").strip().lower() == 'y'
    include_fun_gifs = input("🎉 Include funny GIFs? (y/n): ").strip().lower() == 'y'
    
    return {
        'name': name,
        'description': description,
        'author': author,
        'email': email,
        'license': license_choice,
        'twitter': twitter,
        'farcaster': farcaster,
        'zora': zora,
        'website': website,
        'linkedin': linkedin,
        'github': github,
        'include_badges': include_badges,
        'include_social': include_social,
        'include_install': include_install,
        'include_usage': include_usage,
        'include_contributing': include_contributing,
        'include_fun_gifs': include_fun_gifs,
    }

def get_repo_data():
    """Extract repository information from git"""
    try:
        repo = Repo('.')
        remote_url = None
        if repo.remotes:
            remote_url = repo.remotes.origin.url if repo.remotes.origin else None
        
        # Get last commit
        last_commit = None
        last_commit_date = None
        if repo.head.is_valid():
            latest_commit = repo.head.commit
            last_commit = latest_commit.message.split('\n')[0][:50]
            last_commit_date = latest_commit.committed_datetime.strftime('%Y-%m-%d')
        
        # Get dependencies (basic detection)
        dependencies = []
        if os.path.exists('requirements.txt'):
            try:
                with open('requirements.txt', 'r') as f:
                    for line in f:
                        if '==' in line or '>=' in line:
                            dep = line.split('=')[0].split('>')[0].strip()
                            if dep and not dep.startswith('#'):
                                dependencies.append(dep)
            except:
                pass
        
        return {
            'remote_url': remote_url,
            'last_commit': last_commit,
            'last_commit_date': last_commit_date,
            'dependencies': dependencies[:5]  # Limit to 5 dependencies
        }
    except:
        return {
            'remote_url': None,
            'last_commit': None,
            'last_commit_date': None,
            'dependencies': []
        }

def create_license(license_type, author):
    """Create a license file"""
    licenses = {
        'MIT': f'''MIT License

Copyright (c) {2024} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.''',
        
        'APACHE': f'''Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction,
and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity granting the License.

"Legal Entity" shall mean the union of the acting entity and all
other entities that control, are controlled by, or are under common
control with that entity. For the purposes of this definition,
"control" means (i) the power, direct or indirect, to cause the
direction or management of such entity, whether by contract or
otherwise, or (ii) ownership of fifty percent (50%) or more of the
outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity
exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications,
including but not limited to software source code, documentation
source, and configuration files.

"Object" form shall mean any form resulting from mechanical
transformation or translation of a Source form, including but
not limited to compiled object code, generated documentation,
and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or
Object form, made available under the terms of this License, as
indicated by a copyright notice that is included in or attached to the work
(an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object
form, that is based upon (or derived from) the Work and for which the
editorial revisions, annotations, elaborations, or other modifications
represent, as a whole, an original work of authorship. For the purposes
of this License, Derivative Works shall not include works that remain
separable from, or merely link (or bind by name) to the interfaces of,
the Work and derivative works thereof.

"Contribution" shall mean any work of authorship, including
the original version of the Work and any modifications or additions
to that Work or Derivative Works thereof, that is intentionally
submitted to Licensor for inclusion in the Work by the copyright owner
or by an individual or Legal Entity authorized to submit on behalf of
the copyright owner. For the purposes of this definition, "submitted"
means any form of electronic, verbal, or written communication sent
to the Licensor or its representatives, including but not limited to
communication on electronic mailing lists, source code control systems,
and issue tracking systems that are managed by, or on behalf of, the
Licensor for the purpose of discussing and improving the Work, but
excluding communication that is conspicuously marked or otherwise
designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity
on behalf of whom a Contribution has been received by Licensor and
subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of
this License, each Contributor hereby grants to You a perpetual,
worldwide, non-exclusive, no-charge, royalty-free, irrevocable
copyright license to use, reproduce, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Work, and to
permit persons to whom the Work is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Work.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.''',
        
        'GPL': '''GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>

Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

Preamble

The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works. By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.

This license applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.

For the full GPL-3.0 license text, please visit: https://www.gnu.org/licenses/gpl-3.0.txt'''
    }
    
    if license_type in licenses:
        with open('LICENSE', 'w') as f:
            f.write(licenses[license_type])
        print(f"📄 Created {license_type} license file")
        return True
    return False

def generate_readme(user_input, repo_data, output_path):
    import random
    
    # Random visual themes
    themes = [
        {'color': 'A855F7', 'emoji': '🌟', 'style': 'gradient'},
        {'color': 'FF6B6B', 'emoji': '🚀', 'style': 'modern'},
        {'color': '4ECDC4', 'emoji': '💎', 'style': 'minimal'},
        {'color': 'FFD93D', 'emoji': '✨', 'style': 'bright'},
        {'color': '6C5CE7', 'emoji': '🌙', 'style': 'dark'},
        {'color': 'FF8C42', 'emoji': '🔥', 'style': 'warm'},
        {'color': '00D4FF', 'emoji': '💫', 'style': 'cool'},
    ]
    
    theme = random.choice(themes)
    
    template_str = f'''
<div align="center">

# {theme['emoji']} {{{{ name }}}} {theme['emoji']}

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=2800&pause=2000&color={theme['color']}&center=true&vCenter=true&width=940&lines={{{{ name | replace(' ', '+') }}}};{{{{ description | replace(' ', '+') if description else 'Awesome+Project' }}}};Built+with+❤️+by+{{{{ author | replace(' ', '+') if author else 'Developer' }}}}" alt="Typing SVG" />
</p>

---

{{%- if include_badges -%}}
<p align="center">
  <img src="https://img.shields.io/badge/License-{{{{ license }}}}-blue.svg?style=for-the-badge&logo=license&logoColor=white" alt="License Badge"/>
  {{{%- if repo_data.remote_url -%}}}
  <img src="https://img.shields.io/github/stars/{{{{ repo_data.remote_url | replace('https://github.com/', '') | replace('.git', '') }}}}/style=for-the-badge&logo=github&logoColor=white&color=yellow" alt="GitHub Stars"/>
  <img src="https://img.shields.io/github/forks/{{{{ repo_data.remote_url | replace('https://github.com/', '') | replace('.git', '') }}}}/style=for-the-badge&logo=github&logoColor=white&color=orange" alt="GitHub Forks"/>
  {{{%- endif -%}}}
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Made with Python"/>
  <img src="https://img.shields.io/badge/Version-1.0.0-green?style=for-the-badge&logo=version&logoColor=white" alt="Version"/>
</p>
{{%- endif -%}}

{{%- if include_social -%}}
<p align="center">
  {{{%- if twitter -%}}}<a href="https://twitter.com/{{{{ twitter }}}}"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"/></a>{{{{%- endif -%}}}}
  {{{%- if farcaster -%}}}<a href="https://warpcast.com/{{{{ farcaster }}}}"><img src="https://img.shields.io/badge/Farcaster-8B5CF6?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJDMTMuMSAyIDE0IDIuOSAxNCA0VjIwQzE0IDIxLjEgMTMuMSAyMiAxMiAyMkMxMC45IDIyIDEwIDIxLjEgMTAgMjBWMTRDMTAgMi45IDEwLjkgMiAxMiAyWk0xMiA2QzEzLjEgNiAxNCA2LjkgMTQgOFYxNkMxNCAxNy4xIDEzLjEgMTggMTIgMThDMTAuOSAxOCAxMCAxNy4xIDEwIDE2VjgwQzEwIDYuOSAxMC45IDYgMTIgNloiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPg==" alt="Farcaster"/></a>{{{{%- endif -%}}}}
  {{{%- if zora -%}}}<a href="https://zora.co/{{{{ zora }}}}"><img src="https://img.shields.io/badge/Zora-000000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiByeD0iNCIgZmlsbD0iYmxhY2siLz4KPHRleHQgeD0iMTIiIHk9IjE2IiBmb250LXNpemU9IjE0IiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+UjwvdGV4dD4KPHN2Zz4=" alt="Zora"/></a>{{{{%- endif -%}}}}
  {{{%- if website -%}}}<a href="{{{{ website }}}}"><img src="https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=Firefox&logoColor=white" alt="Website"/></a>{{{{%- endif -%}}}}
  {{{%- if linkedin -%}}}}<a href="https://linkedin.com/in/{{{{ linkedin }}}}"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>{{{{%- endif -%}}}}
  {{{%- if github -%}}}}<a href="https://github.com/{{{{ github }}}}"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>{{{{%- endif -%}}}}
</p>
{{%- endif -%}}

---

## 📖 About

{{{{ description }}}}

{{%- if repo_data.last_commit -%}}
### 🚀 Latest Update
> *{{{{ repo_data.last_commit }}}}^* - {{{{ repo_data.last_commit_date }}}}
{{%- endif -%}}

---

## 🛠️ Tech Stack

{{%- if repo_data.dependencies -%}}
<div align="center">

### Dependencies
{{%- for dep in repo_data.dependencies -%}}
<img src="https://img.shields.io/badge/{{{{ dep }}}}-{theme['color']}?style=for-the-badge&logo={{{{ dep | lower }}}}&logoColor=white" alt="{{{{ dep }}}}"/>
{{%- endfor -%}}

</div>
{{%- endif -%}}

---

## 📊 Stats

{{%- if repo_data.remote_url -%}}
<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username={{{{ repo_data.remote_url | replace('https://github.com/', '') | replace('.git', '') | split('/') | first }}}}&show_icons=true&theme=tokyonight&hide_border=true" alt="GitHub Stats" />

<img src="https://github-readme-streak-stats.herokuapp.com/?user={{{{ repo_data.remote_url | replace('https://github.com/', '') | replace('.git', '') | split('/') | first }}}}&theme=tokyonight&hide_border=true" alt="GitHub Streak" />

</div>
{{%- endif -%}}

---

## 📄 License

This project is licensed under the **{{{{ license }}}} License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**{{{{ author }}}}**
{{%- if email -%}}📧 {{{{ email }}}}{{{%- endif -%}}}

{{%- if website -%}}🌐 [{{{{ website }}}}]({{{{ website }}}}){{{%- endif -%}}

---

{{%- if include_fun_gifs -%}}
## 🎉 Fun Section

<div align="center">

### When your code finally works:
<img src="https://media.giphy.com/media/S9oNGC1E42VT2/giphy.gif" width="300" alt="Celebration GIF"/>

### When you find a bug:
<img src="https://media.giphy.com/media/13d2jHlSlxklVe/giphy.gif" width="300" alt="Bug finding GIF"/>

### When you deploy successfully:
<img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="300" alt="Deploy success GIF"/>

### When you understand the code:
<img src="https://media.giphy.com/media/3o7TKz9bX9v9Kz7ZmM/giphy.gif" width="300" alt="Understanding code GIF"/>

</div>

---

{{%- endif -%}}

<div align="center">

**Made with ❤️ by {{{{ author }}}}**

<img src="https://img.shields.io/badge/Thank%20You-🙏-blue?style=for-the-badge" alt="Thank You"/>

---

*⭐ Star this repo if you found it helpful!*

</div>
'''
    
    template = Template(template_str)
    content = template.render(
        name=user_input['name'],
        description=user_input['description'],
        author=user_input['author'],
        email=user_input['email'],
        license=user_input['license'],
        twitter=user_input.get('twitter', ''),
        farcaster=user_input.get('farcaster', ''),
        zora=user_input.get('zora', ''),
        website=user_input.get('website', ''),
        linkedin=user_input.get('linkedin', ''),
        github=user_input.get('github', ''),
        include_badges=user_input['include_badges'],
        include_social=user_input.get('include_social', False),
        include_install=user_input['include_install'],
        include_usage=user_input['include_usage'],
        include_contributing=user_input['include_contributing'],
        include_fun_gifs=user_input.get('include_fun_gifs', False),
        repo_data=repo_data
    )
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    
    print(f"🎉 Beautiful README generated at {output_path}")
    
    # Create license file if requested
    if user_input.get('license') != 'NONE':
        create_license(user_input['license'], user_input['author'])

def main():
    parser = argparse.ArgumentParser(description="Generate a professional README for your project.")
    parser.add_argument("--output", "-o", default="README.md", help="Output file path (default: README.md)")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode to ask questions")
    
    args = parser.parse_args()
    
    repo_data = get_repo_data()
    
    if args.interactive:
        user_input = get_user_input()
        generate_readme(user_input, repo_data, args.output)
    else:
        # Default values for non-interactive mode
        user_input = {
            'name': 'My Project',
            'description': 'A awesome project',
            'author': 'Developer',
            'email': '',
            'license': 'MIT',
            'twitter': '',
            'farcaster': '',
            'zora': '',
            'website': '',
            'linkedin': '',
            'github': '',
            'include_badges': True,
            'include_social': False,
            'include_install': True,
            'include_usage': True,
            'include_contributing': True,
            'include_fun_gifs': False,
        }
        generate_readme(user_input, repo_data, args.output)

if __name__ == "__main__":
    main()