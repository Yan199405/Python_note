# scrapy 框架安装
- scrapy安装需要的依赖库较多，确保安装之前先安装好依赖环境，尤其是windows平台
    
## windows下安装
- 虚拟环境下安装 
    - windows下我们可以借助Anaconda方便的安装scrapy（虚拟环境）
    - 只需要在Anaconda Prompt下运行命令：
            
          conda install Scrapy
- 专用平台下安装
    - 依次进行以下依赖包的安装
        
          1. wheel
             pip install wheel
          2. lxml
             http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
          3. PyOpenssl
             https://pypi.python.org/pypi/pyOpenSSL#downloads
          4. Twisted
             http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
          5. Pywin32
             https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
             https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32
        注：下载的whl文件直接用：“pip install whl文件位置” 进行安装
        
    - 最后使用pip安装
        - pip install scrapy
        


## linux下安装
- Centos\redhat\fedora
    - 安装依赖
    
          sudo yum groupinstall development tools
          sudo yum install python34-devel epel-release libxslt-devel libxml2-devel openssldevel
          
    - 安装scrapy
          
          pip3 install Scrapy      
    
- Ubuntu\Debian\Deepin
    - 安装依赖
    
          sudo apt-get install build-essential python3-dev libssl-dev libffi-dev libxml2
          libxml2-dev libxslt1-dev zlib1g-dev
    
    - 安装scrapy
          
          pip3 install Scrapy     
    
## Mac OS
- 安装依赖
    
    在MAC上构建scrapy依赖库需要C编译器以及开发头文件，一般由xcode命令安装即可：
         
         xcode-select --install    
    
    - 安装scrapy
          
          pip3 install Scrapy     
    
# 常见错误：
- File "d:\programdata\anaconda3\lib\site-packages\cryptography\hazmat\bindings\openssl\binding.py", line 15, in <module>
    from cryptography.hazmat.bindings._openssl import ffi, lib
ImportError: DLL load failed: 找不到指定的程序。
    - 解决：pip install -I cryptography
    
#  测试安装是否完成 
- 直接运行scrapy测试没有报错即可
- 简单使用
    - 启动一个项目
        
            (base) C:\Users\Administrator>scrapy startproject hello
            New Scrapy project 'hello', using template directory 'd:\programdata\anaconda3\lib\site-packages\scrapy\templates\project', created in:
                C:\Users\Administrator\hello
            
            You can start your first spider with:
                cd hello
                scrapy genspider example example.com
                //创建spider的命令：scrapy genspider baidu www.baidu.com
            
    
        