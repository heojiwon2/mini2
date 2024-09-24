// 여기에서 Chart.js를 사용하여 그래프를 그리는 코드 작성
const churnData = {}; // 고객 이탈 데이터
const totalChargesData = {}; // 총 요금 데이터
const tenureData = {}; // 계약 기간 데이터

// 차트 그리기 함수
function drawCharts() {
    const churnCtx = document.getElementById('churnBarChart').getContext('2d');
    const churnBarChart = new Chart(churnCtx, {
        type: 'bar',
        data: {
            labels: ['이탈', '비이탈'],
            datasets: [{
                label: '고객 수',
                data: [churnData.churnCount, churnData.notChurnCount],
                backgroundColor: ['red', 'green']
            }]
        }
    });

    // 총 요금 차트 그리기
    const totalChargesCtx = document.getElementById('totalChargesBarChart').getContext('2d');
    const totalChargesBarChart = new Chart(totalChargesCtx, {
        type: 'bar',
        data: {
            labels: Object.keys(totalChargesData),
            datasets: [{
                label: '이탈 고객 수',
                data: Object.values(totalChargesData),
                backgroundColor: 'orange'
            }]
        }
    });

    // 계약 기간 도넛 차트 그리기
    const tenureCtx = document.getElementById('tenureDoughnutChart').getContext('2d');
    const tenureDoughnutChart = new Chart(tenureCtx, {
        type: 'doughnut',
        data: {
            labels: Object.keys(tenureData),
            datasets: [{
                data: Object.values(tenureData),
                backgroundColor: ['red', 'orange', 'yellow', 'green']
            }]
        }
    });
}

// 페이지 로드 시 차트 그리기
document.addEventListener('DOMContentLoaded', drawCharts);
