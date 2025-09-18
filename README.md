<div align="center">

# 🚀 Professional README Generator

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=2800&pause=2000&color=2563EB&center=true&vCenter=true&width=940&lines=Generate+Beautiful+READMEs;Professional+Documentation;Automated+Repository+Analysis;Social+Media+Integration" alt="Typing SVG" />
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge&logo=license&logoColor=white" alt="License"/>
  <img src="https://img.shields.io/badge/Version-1.0.0-green?style=for-the-badge&logo=version&logoColor=white" alt="Version"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge&logo=github&logoColor=white" alt="PRs Welcome"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Adrijan-Petek/readme-generator?style=for-the-badge&logo=github&logoColor=white&color=yellow" alt="GitHub Stars"/>
  <img src="https://img.shields.io/github/forks/Adrijan-Petek/readme-generator?style=for-the-badge&logo=github&logoColor=white&color=orange" alt="GitHub Forks"/>
  <img src="https://img.shields.io/github/issues/Adrijan-Petek/readme-generator?style=for-the-badge&logo=github&logoColor=white&color=red" alt="Issues"/>
  <img src="https://img.shields.io/github/last-commit/Adrijan-Petek/readme-generator?style=for-the-badge&logo=github&logoColor=white&color=green" alt="Last Commit"/>
</p>

---

## ✨ Features

<div align="center">

### 🎨 **Visual Excellence**
- **Random Theme Generation**: Daily different visual themes with unique colors and emojis
- **Professional Design**: Clean, modern layout suitable for GitHub profiles and repositories
- **Responsive Badges**: Beautiful shields.io badges with proper styling
- **Animated Elements**: Typing animations and dynamic content

### 🤖 **Smart Automation**
- **Git Repository Analysis**: Automatically extracts project data, dependencies, and commit history
- **License Generation**: Creates complete license files (MIT, GPL, Apache-2.0, BSD-3-Clause)
- **Dependency Detection**: Scans `requirements.txt` and `package.json` for tech stack
- **Social Media Integration**: Links to Twitter/X, Farcaster, Zora, LinkedIn, and GitHub

### � **Rich Content**
- **GitHub Stats Integration**: Repository statistics and contribution graphs
- **Tech Stack Display**: Automatic dependency visualization with badges
- **Latest Updates**: Shows recent commit information
- **Professional Sections**: Installation, usage, contributing guidelines

</div>

---

## 🎯 Use Cases

<div align="center">

### 👤 **For Developers**
- **GitHub Profile READMEs**: Create stunning profile pages with daily visual variations
- **Project Documentation**: Generate professional READMEs for open source projects
- **Portfolio Enhancement**: Showcase your work with beautiful, consistent documentation

### 🏢 **For Teams**
- **Standardization**: Ensure consistent README format across all team projects
- **Onboarding**: Help new team members understand project structure quickly
- **Maintenance**: Keep documentation up-to-date with automated generation

</div>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Adrijan-Petek/readme-generator.git
cd readme-generator

# Install dependencies
pip install -r requirements.txt

# Run in interactive mode
python main.py --interactive

# Or run with default settings
python main.py
```

---

## � Installation

### Prerequisites
- **Python 3.8+**
- **Git** (for repository analysis)
- **Internet connection** (for badge generation)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Adrijan-Petek/readme-generator.git
   cd readme-generator
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python main.py --help
   ```

---

## 💻 Usage

### Interactive Mode (Recommended)

```bash
python main.py --interactive
```

The tool will ask you a series of questions:

#### 📝 **Project Information**
- **Project Name**: Your project's display name
- **Description**: Brief description of what your project does
- **Author Name**: Your full name or organization name
- **Author Email**: Contact email (optional)

#### 📄 **Legal & Licensing**
- **License Type**: Choose from MIT, GPL, Apache-2.0, BSD-3-Clause, or NONE

#### 🌐 **Social Media & Links**
- **Twitter/X Handle**: Your Twitter username (optional)
- **Farcaster Handle**: Your Farcaster username (optional)
- **Zora Handle**: Your Zora username (optional)
- **Website URL**: Your personal/professional website (optional)
- **LinkedIn Username**: Your LinkedIn profile (optional)
- **GitHub Username**: Your GitHub username (optional)

#### ⚙️ **Content Options**
- **Include Badges**: Add license, version, and tech badges
- **Include Social Links**: Add social media profile links
- **Include Installation**: Add installation instructions section
- **Include Usage**: Add usage examples section
- **Include Contributing**: Add contribution guidelines
- **Include Fun GIFs**: Add celebratory GIFs section

### Non-Interactive Mode

```bash
# Generate with default settings
python main.py

# Specify output file
python main.py --output MY_README.md
```

---

## 📊 Generated README Features

### 🎨 **Visual Elements**
- **Dynamic Themes**: 7 different color schemes with unique emojis
- **Animated Headers**: Typing animation with project information
- **Professional Badges**: License, version, and technology badges
- **Social Media Links**: Direct links to your profiles

### 📈 **GitHub Integration**
- **Repository Stats**: Stars, forks, and contribution graphs
- **Latest Commits**: Recent activity and updates
- **Tech Stack**: Automatic dependency visualization
- **Profile Links**: GitHub profile integration

---

## 🎨 Customization

### Theme System

The tool includes 7 beautiful themes:

| Theme | Color | Emoji | Style |
|-------|-------|-------|-------|
| **Gradient** | `#A855F7` | 🌟 | Modern gradient |
| **Modern** | `#FF6B6B` | 🚀 | Clean and minimal |
| **Minimal** | `#4ECDC4` | 💎 | Simple elegance |
| **Bright** | `#FFD93D` | ✨ | Vibrant and energetic |
| **Dark** | `#6C5CE7` | 🌙 | Dark mode friendly |
| **Warm** | `#FF8C42` | 🔥 | Cozy and inviting |
| **Cool** | `#00D4FF` | 💫 | Fresh and calming |

---

## 📈 GitHub Integration

### GitHub Actions Workflow

Create `.github/workflows/generate-readme.yml`:

```yaml
name: Generate README
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Generate README
        run: python main.py --output README.md
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add README.md
          git commit -m "Update README [skip ci]" || echo "No changes to commit"
      - name: Push changes
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

---

## 🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines for details.

### Development Setup

```bash
# Fork and clone
git clone https://github.com/Adrijan-Petek/readme-generator.git
cd readme-generator

# Create feature branch
git checkout -b feature/amazing-feature

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Make your changes
# ...

# Submit pull request
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [`LICENSE`](LICENSE) file for details.

---

## 🙏 Acknowledgments

<div align="center">

### 🛠️ **Built With**
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
</p>

### 📊 **Services Used**
- **Shields.io**: Beautiful badges and shields
- **GitHub Readme Stats**: Repository statistics
- **Readme Typing SVG**: Animated typing effects

### 👥 **Contributors**
<a href="https://github.com/Adrijan-Petek/readme-generator/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Adrijan-Petek/readme-generator" alt="Contributors"/>
</a>

---

<div align="center">

**Made with ❤️ by [Adrijan Petek](https://github.com/Adrijan-Petek)**

<img src="https://img.shields.io/badge/Thank%20You-🙏-blue?style=for-the-badge" alt="Thank You"/>

---

*⭐ Star this repo if you found it helpful!*

</div>