const chart = new Chartist.Line(".ct-chart", {});

const lines = ["a", "b", "c"];

// Grab all the columns
const columnList = document.querySelector(".control-column ul");
const columns = columnList.children;

for (let i = 0, length = columns.length; i < length; i += 1) {
  columns[i].children[0].addEventListener("input", function() {
    updateLines(columns);
  });
}

// Update the lists to be checked
columnList.addEventListener("click", e => {
  if (e.target.tagName === "LI") {
    e.target.classList.toggle("checked");
  }
});

// Get the initial chart data
// function getChartData(queryString = "?n=2013&n=2013&m=AAPL&m=AAL") {
function getChartData(queryString = "?n=2013&n=2013&m=AAL") {
  axios
    .get("/time_series" + queryString)
    .then(res => {
      let timeSeries = res.data;

      console.log(timeSeries)

      const seriesData = [];
      const series = ['AAL', 'AAPL', 'AAP', 'ABBV', 'ABC', 'ABT', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'ADS', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AJG', 'AKAM', 'ALB', 'ALGN', 'ALK', 'ALLE', 'ALL', 'ALXN', 'AMAT', 'AMD', 'AME', 'AMGN', 'AMG', 'AMP', 'AMT', 'AMZN', 'ANDV', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'APC', 'APD', 'APH', 'APTV', 'ARE', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP', 'AYI', 'AZO', 'A', 'BAC', 'BAX', 'BA', 'BBT', 'BBY', 'BDX', 'BEN', 'BF.B', 'BHF', 'BHGE', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRK.B', 'BSX', 'BWA', 'BXP', 'CAG', 'CAH', 'CAT', 'CA', 'CBG', 'CBOE', 'CBS', 'CB', 'CCI', 'CCL', 'CDNS', 'CELG', 'CERN', 'CFG', 'CF', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CINF', 'CI', 'CLX', 'CL', 'CMA', 'CMCSA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF', 'COG', 'COL', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'C', 'DAL', 'DE', 'DFS', 'DGX', 'DG', 'DHI', 'DHR', 'DISCA', 'DISCK', 'DISH', 'DIS', 'DLR', 'DLTR', 'DOV', 'DPS', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DWDP', 'DXC', 'D', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ESRX', 'ESS', 'ES', 'ETFC', 'ETN', 'ETR', 'EVHC', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'FAST', 'FBHS', 'FB', 'FCX', 'FDX', 'FE', 'FFIV', 'FISV', 'FIS', 'FITB', 'FLIR', 'FLR', 'FLS', 'FL', 'FMC', 'FOXA', 'FOX', 'FRT', 'FTI', 'FTV', 'F', 'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GOOGL', 'GOOG', 'GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HII', 'HLT', 'HOG', 'HOLX', 'HON', 'HPE', 'HPQ', 'HP', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IPG', 'IP', 'IQV', 'IRM', 'IR', 'ISRG', 'ITW', 'IT', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'KEY', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KORS', 'KO', 'KR', 'KSS', 'KSU', 'K', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LYB', 'L', 'MAA', 'MAC', 'MAR', 'MAS', 'MAT', 'MA', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MLM', 'MMC', 'MMM', 'MNST', 'MON', 'MOS', 'MO', 'MPC', 'MRK', 'MRO', 'MSFT', 'MSI', 'MS', 'MTB', 'MTD', 'MU', 'MYL', 'M', 'NAVI', 'NBL', 'NCLH', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NOV', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWSA', 'NWS', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'O', 'PAYX', 'PBCT', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PGR', 'PG', 'PHM', 'PH', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PXD', 'PX', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'REGN', 'REG', 'RE', 'RF', 'RHI', 'RHT', 'RJF', 'RL', 'RMD', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCG', 'SCHW', 'SEE', 'SHW', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNI', 'SNPS', 'SO', 'SPGI', 'SPG', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWKS', 'SWK', 'SYF', 'SYK', 'SYMC', 'SYY', 'TAP', 'TDG', 'TEL', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TPR', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSS', 'TWX', 'TXN', 'TXT', 'T', 'UAA', 'UAL', 'UA', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'V', 'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WHR', 'WLTW', 'WMB', 'WMT', 'WM', 'WRK', 'WU', 'WYNN', 'WYN', 'WY', 'XEC', 'XEL', 'XLNX', 'XL', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS'];

      for (let i = 0, length = series.length; i < length; i += 1) {
        const currSeries = series[i];

        // Check if the current series exist
        if (typeof timeSeries[currSeries] !== "undefined") {
          const data = Object.values(timeSeries[currSeries]);
          seriesData.push(data);
        }
      }

      const chartData = {
        labels: Object.values(timeSeries.date).map(utc => {
          const date = new Date(0);
          date.setUTCMilliseconds(Number(utc));
          return `${date.getFullYear()}-${date.getMonth()}`;
        }),
        series: seriesData
      };
      chart.update(chartData);

      updateLines(columnList.children);
    })
    .catch(err => console.error(err));
}

// Updating the chart data
function updateChart() {
  let queryString;
  const items = columnList.children;

  // Get both input fields from the time frame section
  const timeFrames = document.querySelectorAll(".control-date > input");

  // Grab all time ranges
  for (let i = 0, length = timeFrames.length; i < length; i += 1) {
    time = timeFrames[i].value;

    // Start or add to the query string
    if (typeof queryString === "undefined") {
      queryString = "?n=" + time;
    } else {
      queryString += "&n=" + time;
    }
  }

  let currLine = 0;
  // Grab all the checked columns
  for (let i = 0, length = items.length; i < length; i += 1) {
    if (items[i].classList.contains("checked")) {
      // queryString += "&m=" + items[i].innerText.toLowerCase(); #changed this to not lower case
      queryString += "&m=" + items[i].innerText;
    }
  }

  getChartData(queryString);
}

// Update the lines drawn with the correct colors
function updateLines(items) {
  let currLine = 0;
  // Grab all the checked columns
  for (let i = 0, length = items.length; i < length; i += 1) {
    // Only color the checked off lines
    if (items[i].classList.contains("checked")) {
      currentLine = document.querySelector(
        ".ct-series-" + lines[currLine] + " .ct-line"
      );
      currentPoints = document.querySelectorAll(
        ".ct-series-" + lines[currLine] + " .ct-point"
      );
      currentLine.style.cssText =
        "stroke: " + items[i].children[0].value + "!important;";

      // Color every point
      for (let j = 0, length = currentPoints.length; j < length; j += 1) {
        currentPoints[j].style.cssText =
          "stroke: " + items[i].children[0].value + "!important;";
      }
      currLine += 1;
    }
  }
}

getChartData();
