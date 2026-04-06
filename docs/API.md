# 🔧 GLOOM-OX API Documentation

## Command Line Interface

```bash
gloom-ox [OPTIONS] [URL]

Options:
  -u, --update     Update all dependencies
  -d, --dir        Show download directory
  -v, --version    Show version
  -o, --output     Custom output directory
  -q, --quiet      Quiet mode (no banner)
  -h, --help       Show help
```

Python API

Basic Usage

```python
from gloom_ox.core.download_manager import DownloadManagerUnleashed

manager = DownloadManagerUnleashed()
file_path, title = manager.download("https://youtube.com/watch?v=...")
```

With Bypass

```python
from gloom_ox.ui.robot_assistant import RobotAssistant

robot = RobotAssistant()
robot.detect_platform_issue(url, error_message)
robot.show_bypass_progress(bypass_type)
```

Return Codes

Code Meaning
0 Success
1 Download failed
2 Network error
3 Dependency missing

```
