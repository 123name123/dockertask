<p>Чтобы запустить контейнер, войдите в папку с нужным типом файла</p>
<code>cd yaml</code>
<p>Соберите проект</p>
<code>docker build -t yamltest .</code>
<p>Запустите его</p>
<code>docker run -p your_port:80 yamltest </code>
<p>Запрос для тестирования файла</p>
<code>curl -X POST -F "file=@/path/to/file" http://localhost:your_port/get_result</code>