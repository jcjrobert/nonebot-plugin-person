<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-person

_✨ Nonebot2 简易插件随个人，随个群友当幸运观众🤪 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/jcjrobert/nonebot-plugin-person.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-person">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-person.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-person

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-person
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-person
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-person
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-person
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot_plugin_person')

</details>

<details>
<summary>从 github 安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 输入以下命令克隆此储存库

    git clone https://github.com/jcjrobert/nonebot-plugin-person.git

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('src.plugins.nonebot_plugin_person')

</details>

## ⚙️ 配置

可在 nonebot2 项目的`.env`文件中添加下表中的配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| PERSON_SHOW_AVATAR | 否 | true | 是否显示头像，默认显示 |
| PERSON_EXTRA_MESSAGES | 否 | [] | 自定义文案，{name}会替换成Bot昵称，{person}会替换成抽到的人的信息，没有这两项依然能展示 |
| PERSON_EXTRA_MESSAGES_OVERWRITE | 否 | false | 自定义文案是否覆盖已有文案，默认不覆盖 |
| PERSON_AT | 否 | false | 是否at随人对象，将会替换QQ号放在消息结尾 |

## 🎉 使用

随个人

随个人帮我打代码

随个人XXX

...

## 📝 更新日志

<details>
<summary>展开/收起</summary>

### 0.0.3

- 支持AT随人对象

### 0.0.2

- 支持头像显示
- 支持自定义文案，同时支持是否覆盖原文案

### 0.0.1

- 插件初次发布

</details>

## 开源许可

本项目使用[MIT](./LICENSE)许可证开源

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
