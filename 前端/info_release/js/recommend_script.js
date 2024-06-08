$(function() {
    // 从 localStorage 获取搜索参数
    const searchParams = JSON.parse(localStorage.getItem('searchParams'));

    if (searchParams) {
        const queryString = new URLSearchParams(searchParams).toString();

        // 从后端获取推荐信息并显示在页面上
        fetch(`http://8.130.139.193:5000/stu_search?${queryString}`)
        .then(response => response.json())
        .then(data => {
            // 获取表格的主体部分
            const tableBody = document.getElementById('data-table').getElementsByTagName('tbody')[0];
            // 遍历数据并生成表格行
            data.forEach(item => {
                const row = tableBody.insertRow();
                // 根据你的数据库表的字段名创建单元格并填充数据
                const cellId = row.insertCell(0);
                const cellName = row.insertCell(1);
                const cellSex = row.insertCell(2);
                const cellSchool = row.insertCell(3);
                const cellStage = row.insertCell(4);
                const cellSubject = row.insertCell(5);
                const cellTs = row.insertCell(6);
                const cellTe = row.insertCell(7);

                cellId.textContent = item.TR_id;
                cellName.textContent = item.TR_name;
                cellSex.textContent = item.TR_sex;
                cellSchool.textContent = item.TR_school;
                cellStage.textContent = item.TR_stage;
                cellSubject.textContent = item.TR_subject;
                cellTs.textContent = item.TR_s;
                cellTe.textContent = item.TR_e;
                // 如果有更多字段，继续创建单元格
            });
        })
        .catch(error => console.error('Error fetching data:', error));
    } else {
        alert('没有搜索参数。请从主页进行搜索。');
    }
});

function displayRecommendations(data) {
    const recommendationsDiv = document.getElementById('recommendations');
    recommendationsDiv.innerHTML = data.map(item => `
        <div>
            <p>姓名: ${item.name}</p>
            <p>性别: ${item.sex}</p>
            <p>学校: ${item.school}</p>
            <p>科目: ${item.subject}</p>
            <p>阶段: ${item.stage}</p>
            <p>空闲时间: ${item.free_time}</p>
            <p>联系方式: ${item.contact}</p>
        </div>
    `).join('');
}
