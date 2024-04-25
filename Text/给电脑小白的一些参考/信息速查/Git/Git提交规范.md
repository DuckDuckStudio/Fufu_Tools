# Git 提交规范

又名：Git commit message specification<br>

Git commit message specification是一种规范，用于指导开发者编写Git提交信息的格式和内容，以便更好地管理项目的版本历史和代码贡献。通常，一个标准的Git提交消息由三个部分组成：标题、正文和脚注。下面是一个常见的Git提交消息格式：<br>

```
<type>(<scope>): <subject>

<body>

<footer>
```

其中各部分的含义如下：<br>

* `<type>`：表示提交的类型，通常包括以下几种：feat（新功能）、fix（修复bug）、docs（文档变更）、style（代码格式修改，不影响功能的变动）、refactor（代码重构）、test（增加测试）、chore（构建过程或辅助工具的变动）等。
* `<scope>`：表示提交影响的范围，例如模块、组件等。这部分可以省略。
* `<subject>`：简短描述提交的目的，通常不超过50个字符。
* `<body>`：详细描述提交的内容，包括变更的原因、解决的问题、影响的范围等。这部分可以省略。
* `<footer>`：包含一些附加信息，例如关联的Issue号、变更的重要性等。这部分也可以省略。

遵循Git commit message specification能够使提交信息更加清晰、易读，有助于团队协作和版本控制管理。<br>
