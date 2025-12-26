现在大概是这么个情况，框架都搭完了，接下来只需要填充几个py（单测）和一个sh（端到端测试），我留了TODO说大概怎么做，应该都能AI。

0. 之前做的，调整了一下README之类的项目文档修订。

1. 在当前仓库执行代码风格检查并修复了大部分问题。

2. 提供 .pre-commit-config.yaml 和 lint_check.sh 用于代码风格检查。在第一次开发时执行一次lint_check.sh，安装pre-commit，会hook git的commit，在每次commit之前触发一次代码风格检查，从而将代码风格问题左移到开发者端。

3. 增加 pyproject.toml ，为ci环境配置提供前置环境，比如pyyaml。

4. 优化 environment.yml ，原来的就是一坨屎，对于线上ci配环境非常不友好，现在健康很多。

5. 提供 .github/workflows/ci.yaml ，负责启动pytest检查以及启动lint代码风格检查。

6. 具体来讲，ci分为单测和end2end测试......

    6.1. 在tests文件夹里提供了一批以test_开头的文件，pytest会自己找到这些文件并执行test任务，这里包含了全部的单测。 (TODO)

    6.2. 我们额外写了一个bash脚本来做end2end测试，因为end2end需要更复杂的执行逻辑。(TODO)

7. 提供了coverage测试ci的代码覆盖率，用.coveragerc定义需要覆盖的范围

8. merge保护，执行主线仓库commit和Merge后的commit。对比两次执行的输出，确保合入主线的代码不break主线功能。
    这个一般是在主线和merge进来的分支各跑一次end2end，然后把输出重定向到/tmp/log，对比一下输出。
    可以抄一下end2end ci的写法，或者直接懒得做了。（TODO）

9. cd，在.github/workflows/release.yaml，我从lfz之前的仓库里直接拿过来了。
