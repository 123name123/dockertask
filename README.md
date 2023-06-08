<p>Соберите проект</p>
<code>docker build -t mytester .</code>
<p>Запустите его</p>
<code>docker run -p your_port:80 mytester </code>
<p>Запрос для тестирования сериализации</p>
<code>curl -X POST http://localhost:your_port/get_result/type</code>
<p>Могут быть слудующие типы:</p>
<ol>
<li>xml</li>
<li>json</li>
<li>yml</li>
<li>mpk</li>
<li>avro</li>
<li>pickle</li>
</ol>
<p>В ответ прийдёт строка с размером файла и верменем работы</p>