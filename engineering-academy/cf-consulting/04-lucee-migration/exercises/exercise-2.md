# Exercise 2: Extension Replacement

> Replace Adobe ColdFusion-only extensions with Lucee-compatible alternatives.

## Objective

Learn to migrate ACF-specific features to Lucee equivalents.

## Scenario

**Application:** Legal document management system
**Challenge:** Replace cfpdf and cfchart with Lucee-compatible alternatives

## Instructions

### Part 1: PDF Replacement

**Adobe CF Code:**
```cfml
<cfpdf action="read" source="contract.pdf" name="pdfDoc">
<cfpdf action="getInfo" source="pdfDoc" info="author">
<cfpdf action="merge" destination="merged.pdf" source="page1.pdf,page2.pdf">
```

**Lucee Alternative: PDFtk**

```bash
# Install PDFtk
# Linux: apt-get install pdftk
# Mac: brew install pdftk-java
# Windows: Download from pdflabs.com
```

**ColdFusion Code for PDFtk:**
```cfml
// Read PDF info
cfexecute(name="pdftk", arguments="#sourcePDF# dump_data", variable="pdfInfo");
local.author = reReplace(pdfInfo, ".*InfoKey: Author\s*InfoValue:\s*(\S+).*", "\1", "ONE");

// Merge PDFs
cfexecute(name="pdftk", 
          arguments="#sourceDir#/page1.pdf #sourceDir#/page2.pdf cat output #destDir#/merged.pdf",
          variable="result");
```

**Your Task:** Write Lucee-compatible code for:

```cfml
// Extract text from PDF
<cfpdf action="read" source="document.pdf" name="text">
<cfoutput>#text#</cfoutput>
```

Lucee equivalent:
_______________________________________________________________
_______________________________________________________________

### Part 2: Chart Replacement

**Adobe CF Code:**
```cfml
<cfchart format="flash" 
         chartwidth="600" 
         chartheight="400"
         title="Monthly Sales">
    <cfchartseries type="bar" serieslabel="Sales">
        <cfchartdata item="Jan" value="10000">
        <cfchartdata item="Feb" value="15000">
        <cfchartdata item="Mar" value="12000">
    </cfchartseries>
</cfchart>
```

**Lucee Alternative: ChartJS**

```html
<!-- Include ChartJS -->
<script src="chart.js"></script>

<!-- Create canvas -->
<canvas id="salesChart" width="600" height="400"></canvas>

<script>
var ctx = document.getElementById('salesChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar'],
        datasets: [{
            label: 'Sales',
            data: [10000, 15000, 12000]
        }]
    }
});
</script>
```

**Your Task:** Design a CF + JS solution that:

1. Queries sales data from database
2. Passes data to JavaScript
3. Renders ChartJS chart

```cfml
<!--- Query data --->
<cfquery name="monthlySales">
    SELECT month, SUM(amount) as total
    FROM sales
    GROUP BY month
</cfquery>

<!--- Pass to JS --->

_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

### Part 3: Authentication Migration

**Adobe CF Code:**
```cfml
<cfapplication name="LegalApp"
               sessionmanagement="true"
               sessionstorage="mysql"
               setclientcookies="true">
```

**Lucee Alternative: Redis Session Storage**

```cfml
<cfcomponent>
    this.name = "LegalApp";
    this.applicationtimeout = createTimeSpan(7,0,0,0);
    this.sessiontimeout = createTimeSpan(0,0,30,0);
    
    // Lucee: Use Redis for session storage
    this.sessioncluster = true;
    
    function onApplicationStart() {
        // Redis configuration
        application.sessionStore = "redis";
        application.redisConfig = {
            host: "localhost",
            port: 6379
        };
    }
}
```

**Your Task:** Complete the session configuration:

1. Why is Redis better than MySQL for sessions in Lucee?
_______________________________________________________________
2. What Redis commands does Lucee use for sessions?
_______________________________________________________________
3. How do you configure Redis in Lucee Administrator?
_______________________________________________________________

### Part 4: Migration Effort Estimation

| Extension | Migration Effort | Risk | Alternative |
|-----------|-----------------|------|-------------|
| cfpdf | | | PDFtk, iText, External service |
| cfchart | | | ChartJS, Highcharts |
| cfschedule | | | Same syntax |
| cfexchange | | | REST API |
| Session storage | | | Redis |

## Expected Outcome

1. PDF replacement code
2. Chart replacement solution
3. Session storage configuration
4. Effort estimates

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| PDF replacement working | 25 |
| Chart replacement working | 25 |
| Session config appropriate | 20 |
| Effort estimates realistic | 15 |
| Professional presentation | 15 |
| **Total** | **100** |

**Passing Score:** 70/100
