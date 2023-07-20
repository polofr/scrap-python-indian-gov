import unittest
import re
from lxml import etree


def test_regex_0():
    str_res = '''
        
	
	
	
	
	
	
	
	
	
		
	
		<!-- Basic -->
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<!-- Mobile Metas -->
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<!-- Site Metas -->
		<meta name="keywords" content="">
		<meta name="description" content="">
		<meta name="author" content="">
		
		<title>eGramSwaraj</title>
		
		<!-- slider stylesheet -->
		<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.1.3/assets/owl.carousel.min.css">
		
		<!-- bootstrap core css -->
		<link rel="stylesheet" type="text/css" href="/resources/home/css/bootstrap.css">
		
		<!-- fonts style -->
		<link href="https://fonts.googleapis.com/css?family=Poppins:400,700|Roboto:400,700&amp;display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css?family=Crimson+Text&amp;display=swap" rel="stylesheet">
		<!-- Custom styles for this template -->
		<link href="/resources/home/css/style.css" rel="stylesheet">
		<!-- responsive style -->
		<link href="/resources/home/css/responsive.css" rel="stylesheet">
	
	
		<div class="hero_area">
			<!-- header section strats -->
			<header class="header_section">
				<div class="container-fluid">
					<nav class="navbar navbar-expand-lg custom_nav-container ">
						<a class="navbar-brand" href="welcome.do">
							Government of India |&nbsp;<span class="orangefont">Ministry of Panchayati Raj</span>
						</a>
						<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
							<span class="navbar-toggler-icon"></span>
						</button>
						<div class="collapse navbar-collapse" id="navbarSupportedContent">
							<div class="d-flex ml-auto flex-column flex-lg-row align-items-center mr-0">
								<ul class="navbar-nav navbar-right">
									<li class="nav-item active">
										<a class="nav-link" href="welcome.do">Home <span class="sr-only">(current)</span></a>
									</li>
									<!-- <li class="nav-item">
										<a class="nav-link" href="contact.html">Contact us</a>
									</li> -->
								</ul>
							</div>
						</div>
					</nav>
				</div>
			</header>
			<!-- end header section -->
			<!-- slider section -->
			<section class=" slider_section position-relative">
				<div class="slider_bg-container"></div>
				<div class="slider-container">
					<div class="detail-box">
						<div class="d-flex-inline">
							<img src="/resources/home/images/logo.png" alt="eGramSwaraj" class="invert-black float-left">
							<h1 class="mt-1 mb-0 text-left">
								eGramSwa<span class="orangefont">raj</span>
							</h1>
							<h5 class="text-justify">
								Simplified Work Based Accounting Application for <span class="orangefont">Panchayati Raj</span>
							</h5>
						</div>
					</div>
				</div>
			</section>
			<!-- end slider section -->
		</div>
	
	
  <script type="text/javascript" src="/resources/home/js/jquery-3.4.1.min.js"></script>
  <script type="text/javascript" src="/resources/home/js/bootstrap.js"></script>
	
	
	






<title>PES | Approve Action Plan Report</title>


<script type="text/javascript" language="javascript" src="/dwr/engine.js"></script>
<script type="text/javascript" language="javascript" src="/dwr/util.js"></script>
<script type="text/javascript" src="/dwr/interface/captchaValidator.js"></script>
<script type="text/javascript" src="/resources/js/captcha.js"></script>
<script language="JavaScript" src="resources/js/fusioncharts.js"></script>
<script language="JavaScript" src="resources/js/fusioncharts.charts.js"></script>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  
<script type="text/javascript">
var captchaValue=  '1f8p3u';
</script>
 

<script>
$(document).ready(function(){
    // Add minus icon for collapse element which is open by default
    $(".collapse.show").each(function(){
    	$(this).prev(".card-header").find(".fa").addClass("fa-minus").removeClass("fa-plus");
    });
    
    // Toggle plus minus icon on show hide of collapse element
    $(".collapse").on('show.bs.collapse', function(){
    	$(this).prev(".card-header").find(".fa").removeClass("fa-plus").addClass("fa-minus");
    }).on('hide.bs.collapse', function(){
    	$(this).prev(".card-header").find(".fa").removeClass("fa-minus").addClass("fa-plus");
    });
});

</script>
<script type="text/javascript">

	
var barChartContainer1="barChartDivId1";
var title1="Focus Area wise GP Plan";
var yAxisTitle1="Allocation";


 $(document).ready(function () {
	 google.charts.load('41', {'packages':['corechart']});
     google.charts.setOnLoadCallback(populatePieChart); 

     
	var focusAreaList= '';
	 var gpdpData1='';
	 var ffcData1='';
 	 
 
	drawBarChart(gpdpData1,ffcData1,focusAreaList,barChartContainer1,title1,yAxisTitle1);
	 
    });
 function populatePieChart() {  
 	
 	var data='';     	
 	drawPieChartFn(data);
 }
 function drawPieChartFn(data){
		   	 var jsonData = jQuery.parseJSON(data);     
			   	 var data = google.visualization.arrayToDataTable(
			        	jsonData);

			   		var options = {
			   	          title: 'Sector Wise Planned Outlay(Tied+Untied)',
			   	         
			   	        };

			        var chart = new google.visualization.PieChart(document.getElementById('piechartDivId1'));

			        chart.draw(data, options);
	          }   
  	
    
 
 function drawBarChart(gpdpData,ffcData,focusAreaList,container,title,yAxisTitle)
 {
	FusionCharts.ready(function () {
		var focusAreaWiseBarChart = new FusionCharts(
		{
		"type": "mscolumn3d",
		"renderAt":container,
		"width": "100%",
		"height": "100%",
		"dataFormat": "json",
					"dataSource": {
							"chart": {
							"caption": "",
							"subCaption": "",
							"xAxisName": "Scheme Name",
							"yAxisName": yAxisTitle,
							"numberPrefix": "",
							"paletteColors": "#ff0000,#0000ff,#f2c500",
							"bgColor": "#fef9f3",                
							"showBorder": "0",
							"showCanvasBorder": "0",
							"usePlotGradientColor": "0",
							"plotBorderAlpha": "10",
							"legendBorderAlpha": "0",
							"legendBgAlpha": "0",
							"legendShadow": "1",
							"showHoverEffect" : "1",
							"valueFontColor": "#000",
							"rotateValues": "1",
							"placeValuesInside": "1",
							"divlineColor": "#999999",
							"divLineIsDashed": "1",
							"divLineDashLen": "1",
							"divLineGapLen": "1",
							"canvasBgColor": "#ffffff",
							"captionFontSize": "14",
							"subcaptionFontSize": "14",
							"subcaptionFontBold": "0"
							},
							"categories": [
												{
												"category": jQuery.parseJSON(focusAreaList)
												}
										],
					"dataset": [
					{
					"seriesname": "Planned Outlay",
										"data":  jQuery.parseJSON(gpdpData)
					},
					{
					"seriesname": "Amount Allotted",
										"data": jQuery.parseJSON(ffcData)
					}
					]
					       }
		});
focusAreaWiseBarChart.render();
removeCredit();
});
	 
	 
 }
 function removeCredit(){
     $('[class*="creditgroup"]').remove();
	}
	
        
    	function onCancel(){	
			
		
			    	window.location.href="welcome.do";
			        }
			    
			
			
			
			
	
 function getreport(state_cd,level,fyear,statenm){
	 
	 
	 $("#levelId").val(level);
	 $("#stateId").val(state_cd);
	 $("#fnyearId").val(fyear); 
	 $("#statenmId").val(statenm); 
var formId = document.getElementById("approveActionPlanId");
formId.method="POST";
formId.action="approveActionPlanData.do";
formId.submit();		
} 
 
  
 function getdatat(level){
	 $("#levelId").val(0);

	 $("#accordionflgId").val(level);
	 var captchaVal = $("#captchaAnswer").val();
	 var fy = document.getElementById("fyearid").value;
	 document.getElementById("fnyearId").value=fy;
	 var e = document.getElementById("fyearid");
	 var strUsertext = e.options[e.selectedIndex].text;
	 document.getElementById("planyearid").value = strUsertext;
	
	 if(fy==-1 || fy=='')
	 {
	 $("#activityTypeError").css("display","block");
		$("#fyearid").focus(); 
		return false;
	}
	 
	 if(captchaVal == "" || captchaVal == null) {
		 $("#captchaAnswer_error").css("display","block");
			$("#captchaAnswer").focus(); 
			return false;
	} 	  
			
			   else {
					 var status = validateCaptcha(captchaVal);

			     if(status) {
			    	 refreshCaptcha();
				   var formId = document.getElementById("approveActionPlanId");
				   formId.method="POST";
				   formId.action="approveActionPlanData.do";
				   formId.submit();	
				 } else {
					
			    	 refreshCaptcha();

					 $("#captchaAnswer_errors").css("display","block");
					$("#captchaAnswer").focus(); 
					// refreshCaptcha();
						return false;
					
				
				 }
					
			}
				


		
}  
 function gebackagain(level,finyear){
	 $("#accordionflgId").val(level);
	 $("#fnyearId").val(finyear); 
	 $("#levelId").val(0);

var formId = document.getElementById("approveActionPlanId");
formId.method="POST";
formId.action="approveActionPlanData.do";
formId.submit();		
} 

/*  function getbackreport(state_cd,level,fyear,localbodycd){
		 $("#stateId").val(state_cd);
		 $("#fnyearId").val(fyear);
        	 $("#accordionflgId").val(level);
        	 $("#zpcdId").val(null);
        	 $("#bpcdId").val(null);
        	 $("#local_body_typ_cdid").val(localbodycd);
        	 var formId = document.getElementById("approveActionPlanId");
        	 formId.method="POST";
        	 formId.action="approveActionPlanData.do";
        	 formId.submit();	
 } */
 
 function getbackreport(state_cd,level,fyear,statenm){
	 
	 $("#accordionflgId").val(level);

	 $("#stateId").val(state_cd);
	 $("#fnyearId").val(fyear); 
	 $("#zpcdId").val(null);
	 $("#bpcdId").val(null);
	 $("#gpcdId").val(null);

	 
	 $("#statenmId").val(statenm); 
var formId = document.getElementById("approveActionPlanId");
formId.method="POST";
formId.action="approveActionPlanData.do";
formId.submit();		
} 
 
 
 
 
 function getplanView(plan_code,gp_code,level,stulevl,zpnme,bpnme,gpname,localbodytypcd){
	 $("#accordionflgId").val(level);
	 $("#gpnameid").val(gpname);
	 $("#zpnameid").val(zpnme);
	 $("#bpnameid").val(bpnme);
	 $("#local_body_typ_cdid").val(localbodytypcd);
	 //$("#levelId").val(stulevl);

	 $("#planId").val(plan_code);
	 $("#gpcdId").val(gp_code); 
var formId = document.getElementById("approveActionPlanId");
formId.method="POST";
formId.action="approveActionPlanData.do";
formId.submit();		
} 
 
 
 function getplanViewpdf(plan_code,gp_code,level,stulevl,zpnme,bpnme,gpname,localbodytypcd){
	 $("#accordionflgId").val(level);
	 $("#gpnameid").val(gpname);
	 $("#zpnameid").val(zpnme);
	 $("#bpnameid").val(bpnme);
	 $("#local_body_typ_cdid").val(localbodytypcd);
	 //$("#levelId").val(stulevl);
	 

	 $("#planId").val(plan_code);
	 $("#gpcdId").val(gp_code); 
var formId = document.getElementById("approveActionPlanId");
formId.method="POST";
formId.action="approveActionPlanPdf.do";
formId.submit();		
} 
 
 
 
 
 
 
 
 function exportF(elem) {
	  var table = document.getElementById("tabledata");
	  var html = table.outerHTML;
	  var url = 'data:application/vnd.ms-excel,' + escape(html); // Set your html table into url 
	  elem.setAttribute("href", url);
	  elem.setAttribute("download", "ApprovedActionPlanReport.xls"); // Choose the file name
	  return false;
	}
	
function imprimir() {
   var divToPrint=document.getElementById("tabledata");
   newWin= window.open("");
   newWin.document.write(divToPrint.outerHTML);
   newWin.print();
   newWin.close();
}

  
 
function exportFile(elem) {
	  var table = document.getElementById("statewise-report");
	  var html = table.outerHTML;
	  var url = 'data:application/vnd.ms-excel,' + escape(html); // Set your html table into url 
	  elem.setAttribute("href", url);
	  elem.setAttribute("download", "ApprovedActionPlanReport.xls"); // Choose the file name
	  return false;
	}
	
function printfile() {
 var divToPrint=document.getElementById("statewise-report");
 newWin= window.open("");
 newWin.document.write(divToPrint.outerHTML);
 newWin.print();
 newWin.close();
}
 
 
 
 function goback(level){
	 $("#accordionflgId").val(level);
	 $("#levelId").val(5);

var formId = document.getElementById("approveActionPlanId");
formId.method="POST";
formId.action="approveActionPlanData.do";
formId.submit();		
} 
 

 
 function getbackgpreport(state_cd,level,fyear,zp_cd,bp_cd){
	 $("#levelId").val(level);
	 $("#accordionflgId").val(level);

	 $("#stateId").val(state_cd);
	 $("#fnyearId").val(fyear); 
	 $("#zpcdId").val(zp_cd); 
	 $("#bpcdId").val(bp_cd); 
	 
var formId = document.getElementById("approveActionPlanId");
formId.method="POST";
formId.action="approveActionPlanData.do";
formId.submit();		
} 
 function getgpreport(state_cd,level,fyear,zp_cd,bp_cd,typcod){
	 $("#levelId").val(level);
	 $("#stateId").val(state_cd);
	 $("#fnyearId").val(fyear); 
	 $("#zpcdId").val(zp_cd); 
	 $("#bpcdId").val(bp_cd);
	 $("#local_body_typ_cdid").val(typcod);

	 $("#accordionflgId").val(3);
var formId = document.getElementById("approveActionPlanId");
formId.method="POST";
formId.action="approveActionPlanData.do";
formId.submit();		
 }
 
 

function Back() {
	  window.history.back();
	}


</script>
<style>
.accordion .card-header .btn-link:not(.collapsed) {
    background-color: #f9e3a1;
}
.paichart-cntr .nav-tabs li a.expndr {background-color:#ddd;}
.paichart-cntr .nav-tabs { border-bottom: 2px solid #DDD; }
   .paichart-cntr .nav-tabs > li.active > a, 
   .paichart-cntr .nav-tabs > li.active > a:focus, .paichart-cntr .nav-tabs > li.active > a:hover { border-width: 0; }
 .paichart-cntr   .nav-tabs > li > a { border: none; color: #666; }
     .paichart-cntr   .nav-tabs > li.active > a, .nav-tabs > li > a:hover { border: none; color: #ef800d !important; background: transparent; }
     
     .paichart-cntr   .nav-tabs > li > a::after
      { content: ""; background: #002e5b; height: 2px; position: absolute; width: 100%; left: 0px;
       bottom: -1px; transition: all 250ms ease 0s; transform: scale(0); }
  .paichart-cntr  .nav-tabs > li.active > a::after, .nav-tabs > li:hover > a::after { transform: scale(1); }
.paichart-cntr .tab-nav > li > a::after { background: #21527d none repeat scroll 0% 0%; color: #fff; }
.paichart-cntr .tab-pane { padding: 15px 0; }
.paichart-cntr .tab-content{padding:20px}

.paichart-cntr .card {background: transparent; margin-bottom: 10px; }
</style>
 
 <section id="reports" class="main-reports py-3">
 	<div class="container nav-reports">
 

			<form id="approveActionPlanId" action="approveActionPlanData.do" method="POST">
                      
                      
                        <input id="stateId" name="state_code" type="hidden" value="27"> 
                         <input id="fnyearId" name="plan_year" type="hidden" value="2020">
                          <input id="levelId" name="status_Level" type="hidden" value="3">
                          <input id="zpcdId" name="zp_code" type="hidden" value="">
                          <input id="bpcdId" name="bp_code" type="hidden" value="">
                          <input id="gpcdId" name="gp_code" type="hidden" value="167703">
                          <input id="planId" name="plan_code" type="hidden" value="2654103">
                          <input id="accordionflgId" name="accordionflg" type="hidden" value="5">
                         <input id="planyearid" name="planyrflg" type="hidden" value="2020-2021">
                           <input id="local_body_typ_cdid" name="local_body_typ_cd" type="hidden" value="3">
                            <input id="gpnameid" name="gpname" type="hidden" value="ANANDWADI">
                             <input id="zpnameid" name="zpname" type="hidden" value="AHMEDNAGAR">
                              <input id="bpnameid" name="bpname" type="hidden" value="JAMKHED">
                                   <input id="statenmId" name="state_nam" type="hidden" value="MAHARASHTRA">
                                     <input id="flagpdf" name="flagpdf" value="1" type="hidden">
                                      
                                                    
                         
	
                          
                          <div class="row">
		<div class="col-12 text-center">
		<h5 class="mainHeading heading_black cursor-pointer mx-auto">

Approved Action Plan Report 


2020-2021





 </h5></div>
			</div>
                          

	 
                      
                       
                                                        
                                                        
                                                        
                       <div class="row">
			<div class="col-12 tab-content">		
			 <div class="card">
                         <div class="card-header">
			  <div class="row">
				<div class="col-12">
								<div class="float-right"> 
						 
				              <button onclick="javascript:getplanViewpdf('2654103','167703',5,4,'AHMEDNAGAR','JAMKHED','ANANDWADI','3');" class="btn btn-danger">Export to PDF</button>
				               
				               
						  
				
								  
				
				</div>
				<div class="float-left"> 
				
				                                                        
					    
			</div>
				</div>
				
				 <div class="card-body">
                	 <div class="table-responsive">
					     <table class="table table-striped table-bordered table-hover w-100">
					<thead class="bg-dark text-white">
				<tr>
				<th align="left"><b>Plan Year</b></th>
				<th align="left"><b>State</b></th>	
			
				<th align="left"><b>District Panchayat &amp; equivalent</b></th>
								                    	  
				
				<th align="left"><b>Block Panchayat &amp; equivalent </b></th>
				<th align="left"><b>Village Panchayat &amp; equivalent </b></th>
				
				  	  
				
			</tr>
			<tr class="tblRowB">
					<th align="left"><esapi:encodeforhtml>2020-2021</esapi:encodeforhtml></th>	
			
			
				<th align="left"><esapi:encodeforhtml>MAHARASHTRA </esapi:encodeforhtml></th>	
				
					

				<th align="left"><esapi:encodeforhtml>AHMEDNAGAR</esapi:encodeforhtml></th>


	
				                    	  
				
				
				
					

				<th align="left"><esapi:encodeforhtml>JAMKHED</esapi:encodeforhtml></th>


	
	

				<th align="left"><esapi:encodeforhtml>ANANDWADI</esapi:encodeforhtml></th>


	
				
				
					 
				
			
				
			</tr>
 </thead></table>    
 </div>      </div>
 </div>
				
			  </div>
			       
                      <!-- level 5 starts -->
                    <div class="row" id="report-l5"><div class="col-12">  <div class="accordion tab-content" id="accordion">

                    <div class="card">
            <div class="card-header p-0" id="headingFirst">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link collapsed  w-100 text-left" data-toggle="collapse" data-target="#collapseFirst">
                    <i class="fa fa-plus  float-right"></i>SECTION 1 :Plan Summary</button>                     
                </h2>
            </div>
            <div id="collapseFirst" class="collapse" aria-labelledby="headingFirst" data-parent="#accordion">
                <div class="card-body">
                	 <div class="table-responsive">
                	 
                	 <table class="table table-bordered table-striped table-hover">
<thead class="bg-dark text-white font10px"><tr>

<!-- <th class="text-center" rowspan="3">Village Panchayat & equivalent</td>  -->

<th class="text-center" colspan="8">
	Total Amount Allotted (In Rs.)</th>
		
<th class="text-center" colspan="10">
	Total Planned Outlay (In Rs.)</th>


</tr>
<tr>

<th class="text-center" colspan="8">
	</th>
		<!-- 
<th class="text-center" rowspan="3">Own Fund
	</th> -->

<th class="text-center" colspan="10">
	</th>
		
<!-- <th class="text-center" rowspan="3">Own Fund
	</th> -->
<!-- <th align="left" rowspan="3">Beneficiary Contribution
	</th> -->	

</tr>

<tr>	

<th class="text-center" colspan="4">Tied
	</th>
 <th class="text-center" colspan="4">Untied
	</th> 

<th class="text-center" colspan="5">Tied
	</th>
<th class="text-center" colspan="5">Untied
	</th>
	
</tr>

<tr>


<th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>


 <th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th> 


<th class="text-center" colspan="2">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>


<th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>
	
</tr>
</thead><tbody>

<tr>
<!-- <td align="left"  >CHINNA KOMERLA</td>  -->








</tr>

</tbody></table>
					
                	 </div>
                
                </div></div></div>
        <div class="card">
        <!--section 1 ends  -->
            <div class="card">
            <div class="card-header p-0" id="headingTwo">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link w-100 text-left collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false">
                    <i class="fa float-right fa-plus"></i>SECTION 2 : Sectoral View</button>
                </h2>
            </div>
            <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion" style="">
                <div class="card-body">
                <div class="table-responsive">
									
										<table class="table table-bordered table-striped table-hover">
<thead class="bg-dark text-white font10px"><tr>

<th class="text-center" width="2%" rowspan="4">

	S.No.</th>

<th class="text-center" width="48%" rowspan="4">
	Sector</th>
	
<th class="text-center" colspan="10">
	Planned Outlay</th>
			
</tr>
<tr>
 
<th class="text-center" colspan="8">
 Scheme</th>
         
<!-- <th  class="text-center" rowspan="3">
 Own Fund</th>    
<th  class="text-center" rowspan="3">
 Beneficiary Contribution</th>  -->  
</tr>
<tr>
 
<th class="text-center" colspan="4">
	Tied</th>
<th class="text-center" colspan="4">
	Untied</th>
					
</tr>
<tr>

<th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>


<th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>
                     
</tr>	
</thead>
<tbody>



	
	
	
	
	
	






<tr>

<td align="left" width="2%"></td>
<td align="left" width="48%">
	<strong>Total</strong>
</td>




<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>

<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
</tbody></table></div>
<!--   <div class=" col-lg-6 col-md-12">
      <div class="row inrmapcntr">
             
       <div class="paichart-cntr">
        <div id="piechartDivId1" style="width: 100%; height: 220px;"></div>   
     
       
	      	
		</div>
             
       </div> 
       
       
      </div> -->
      
      <div class="row">
             <div class="col-lg-12 text-center">
		                                   
		    <div id="piechartDivId1" class="text-center" width="900px" height="450px" style="margin:0 auto;display:inline-block;"></div>
       </div>
       </div>
      
      
      
     </div>
     
     
    
     
     
                </div></div></div><!-- section  2 ends -->
            <div class="card">
            <div class="card-header p-0" id="headingThree">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link collapsed  w-100 text-left" data-toggle="collapse" data-target="#collapseThree">
                    <i class="fa fa-plus  float-right"></i>SECTION 3 : Scheme View</button>                     
                </h2>
            </div>
            <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
                <div class="card-body">
                <div class="table-responsive">
									
										<table class="table table-bordered table-striped table-hover">
<thead class="bg-dark text-white font10px"><tr>
<th class="text-center" width="2%" rowspan="3">
	S.No.</th>	
<th class="text-center" width="24%" rowspan="3">
	Scheme Name</th>
<th class="text-center" width="24%" rowspan="3">
	Component Name</th>
	
<th class="text-center" width="25%" colspan="8">
	Amount Allotted</th>
<th class="text-center" width="25%" colspan="8">
	Planned Outlay</th>	
			
</tr>	
<tr>


<th class="text-center" colspan="4">
Tied</th>
<th class="text-center" colspan="4">
	Untied</th>

<th class="text-center" colspan="4">
Tied</th>
<th class="text-center" colspan="4">
	Untied</th>
			

</tr>
<tr>


<th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>

<th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>


<th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>


<th class="text-center">SC</th>
<th class="text-center">ST</th>
<th class="text-center">General</th>
<th class="text-center">Total</th>
   
</tr>

</thead><tbody>




<tr>




<td align="left" width="2%"></td>
<td align="left" colspan="2" width="48%"><strong>Total</strong></td>
<td align="right"></td>
<td align="right"></td>	
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>	
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>	
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td> 

</tr>
</tbody></table></div>

    
      <div class="row">
             <div class="col-lg-12" style="padding:0px;">
       	<h4 class="text-center text text-primary">Scheme Wise Actual Allocation v/s Planned OUtlay</h4><hr>
		                                   
		    <div id="barChartDivId1" style="width:98%; height: 520px;margin:0 auto;"></div>
       </div>
       </div>


                
                </div></div></div><!--section 3 ends  -->
                
            <div class="card">
            <div class="card-header p-0" id="headingFour">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link collapsed  w-100 text-left" data-toggle="collapse" data-target="#collapseFour">
                    <i class="fa fa-plus  float-right"></i>SECTION 4: Priority Wise Activity Details</button>                     
                </h2>
            </div>
            <div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordion">
                <div class="card-body">
            <div class="table-responsive">
										<table class="table table-bordered table-striped table-hover">
	<thead class="bg-dark text-white font10px"><tr>
		<th class="text-center" width="1%" rowspan="2">
			S.No.</th>
			<th class="text-center" width="16%" rowspan="2">Activity Code</th>
		<th class="text-center" width="16%" rowspan="2">
			Name of Activity</th>	
			
		<th class="text-center" width="15%" rowspan="2">
			Activity Description</th>	
		<th class="text-center" width="10%" rowspan="2">
			Activity For</th>				
		<th class="text-center" width="12%" rowspan="1">
			Sector</th>	
		 <th class="text-center" width="12%" rowspan="1">
		Mgnrega Activity category</th> 
		<th class="text-center" width="8%" rowspan="1">
			Location of Asset</th> 
		<th class="text-center" width="8%" rowspan="1">
			Estimated Cost</th>				
			
		<th class="text-center" rowspan="2">
			Total Duration</th>
   <th class="text-center">Scheme Name</th>
<th class="text-center">General Fund</th>
	<th class="text-center">SC Fund</th>
	<th class="text-center">ST Fund</th>

																		</tr>
	
	
	
</thead>
	<tbody>
	
	
		
		
		
	
	
	
	<tr>
			<td align="left" border="1" colspan="1"></td>	
	
		<td align="left" border="1" colspan="7"><strong>Total</strong></td>	
		

 	
 


		 	
				
		<td align="right" border="1" width="8%" rowspan="1">0</td>
	
		
	
		
		<td align="left" border="1"></td>
		
	 <td align="left"></td>
	<td align="right">0</td>
	<td align="right">0
				</td>
				<td align="right">
				0
				</td>

	
		
		
		 </tr>

					
	
		  
          
	
	
	</tbody></table></div>
           
            </div></div></div><!-- Section ends 4  -->
             
          
         
            
           <!-- section 5 ends -->
							
            
            
            </div><!-- accordion ends -->
            </div></div>
          
            </div>
                         <div style="text-align: center">
                       <a href="http://egramswaraj.gov.in"><strong>http://egramswaraj.gov.in</strong></a><br>

                         <strong>Report Generated on 23/12/2020 12:00:24 AM and data is entered and managed by State Panchayati Raj Deparments and Panchayats</strong>
                         </div>
            </div>
              <div class="float-right" style="margin-top:10px;">
						<button type="button" class="btn btn-danger" onclick="onCancel();">
								<i class="fa fa-times"></i>&nbsp;Close
						</button></div>
            </div>
            </form></div>
            

            
            
						  
						





			
			</section>
 
	<footer>
	<div class="container">
		<p>
			 Contents on this website are owned,updated and managed by the Panchayats and State Panchayati Raj Department as a part of e-Panchayat MMP of 
			<a class="foot_link" href="https://www.panchayat.gov.in/">
			Ministry of Panchayati Raj</a>. Site is technically
			designed, hosted and maintained by <a class="foot_link" href="https://www.nic.in/">
			<img src="/resources/home/images/nic.png" style="width: 120px; float: right" class="img-fluid" title="NIC">&nbsp;National Informatics Centre (NIC)</a>
		</p>
		<ul class="list-inline">
					<li class="list-inline-item"><a href="#" data-toggle="modal" data-target="#quickModal" id="One" onclick="allPolicies(this.id)">Terms &amp; Conditions</a></li>
					<li class="list-inline-item"><a href="#" data-toggle="modal" data-target="#quickModal" onclick="allPolicies(this.id)" id="Two">Privacy Policy</a></li>
					
					 <li class="list-inline-item"><a href="#" data-toggle="modal" data-target="quickModal" id="Three" onclick="allPolicies(this.id)">Web policy</a></li>
					<li class="list-inline-item"><a href="#" data-toggle="modal" data-target="#quickModal" onclick="allPolicies(this.id)" id="Four" alt="Contact us">Contact us</a></li>
					<li class="list-inline-item"><a href="#" data-toggle="modal" data-target="#quickModal" onclick="allPolicies(this.id)" id="Five" alt="Web Information Manager">Web Information Manager</a></li>
				</ul>
		<p>Last reviewed and updated on June 27, 2020</p>
	</div>
</footer>


<!-- The Modal -->
<!-- <div class="modal" id="loginModal" style="z-index: 99999;">
  <div class="modal-dialog">
    <div class="modal-content" style="background-color:transparent;border:none;">


      Modal body
      <div class="modal-body"> <button type="button" class="close" data-dismiss="modal" 
			style="color:#fff;margin-top:30px;position:absolute;right:0;">&times;</button>         
			<iframe style="border:none;width:100%;height:500px;" src="login.htm?x=nonpopup" id="loginPopupFrame" ></iframe>
      </div>

      Modal footer
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
      </div>

    </div>
  </div>
</div>
 -->

<div class="modal fade" id="quickModal" role="dialog">
		<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">x</span>
					</button>
			</div>
				<div class="modal-body">
					<div class="row footer-row-padding footer-modal">
						<div class="col-12">
						<div class="accordion" id="accordionExample">
        <div class="card">
            <div class="card-header  p-0" id="headingOne">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link collapsed  w-100 text-left" data-toggle="collapse" data-target="#collapseOne">
                    <i class="fa fa-plus float-right"></i>Terms and Conditions</button>									
                </h2>
            </div>
            <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
                <div class="card-body">
                  <p>The following terms and conditions will apply if you
													wish to use the Internet for availing a service. Please go
													through the conditions carefully and if you accept them,
													you may register yourself and transact on the site. On
													using this site for service delivery, you are deemed to
													have agreed to the terms and conditions set forth below. If
													You do not agree with all these terms and conditions, you
													must not transact on this Website.</p>
												<p>If a user violates the terms and conditions
													Government (service owner) reserves the right to deactivate
													all such user registration and cancel any or all services
													requested without any notice. Garbage / Junk values in
													profile may lead to Deactivation.</p>
												<p>Operationalization of this agreement is subject to
													existing laws and legal processes of the respective
													Government, and nothing contained in this agreement is in
													derogation of Government's right to comply with law
													enforcement requests or requirements relating to your use
													of this Web Site or information provided to or gathered by
													this site with respect to such use. You agree that
													Government may provide details of your use of the Web Site
													to regulators or police or to any other third party, or in
													order to resolve disputes or complaints which relate to the
													Web Site, at Governmentâs complete discretion.</p>
												<p>This agreement is made between: respective service
													owner department of the respective government who has
													configured the serviceGovernment ('Us') and The
													User ('You'), the individual, whose details are
													set out in the Portal User Creation page.</p>
												
												<p>
													<strong>User Creation</strong>
												</p>
												<p>You are responsible for maintaining the
													confidentiality of the password and account, and are fully
													responsible for all activities that occur under your
													password or account. Complaints Procedure</p>
												<p>You can reach us on the contact details given in the
													'Contacts' option given in the login page.</p>
												<p>Your obligations</p>
												<p>
													<strong>General Obligations:</strong>
												</p>
												<p>You shall access web site only for lawful
													purposes and you shall be responsible for complying with
													all applicable laws, statutes and regulations in connection
													with the use of Government web site. This Website is for
													your personal or commercial use by approved kiosks. You
													shall not modify, copy, distribute, transmit, display,
													perform, reproduce, publish, license, create derivative
													works from, transfer or sell any information, or services
													obtained from this Website. You shall not create a
													hypertext link to the Website or "frame" the
													Website, except with the express advance written permission
													of the Government.</p>
												<p>
													<strong>Information Provided</strong>
												</p>
												<p>The information you provide in the Registration page
													must be complete and accurate. Government 00. reserves the
													right at all times to disclose any information as deems
													necessary to satisfy any applicable law, regulation, legal
													process.</p>
												<p>
													<strong>Termination</strong>
												</p>
												<p>We may at any time at our sole discretion and without
													giving any reason or any prior notice terminate or
													temporarily suspend your access to all or any part of the
													web site.</p>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header p-0" id="headingTwo">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link collapsed w-100 text-left" data-toggle="collapse" data-target="#collapseTwo">
                    <i class="fa fa-plus  float-right "></i>Privacy Policy</button>
                </h2>
            </div>
            <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
                <div class="card-body">
                <p>The Government will have complete discretion to share
													the details of your use of the Web Site and/ or data
													entered by you with regulators or with any other third
													party, or in order to resolve disputes or complaints which
													relate to the Web Site.</p>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header p-0" id="headingThree">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link collapsed  w-100 text-left" data-toggle="collapse" data-target="#collapseThree">
                    <i class="fa fa-plus  float-right"></i>Web Policy</button>                     
                </h2>
            </div>
            <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">
                <div class="card-body">
                <p>The following terms and conditions will apply if you
													wish to use the Internet for availing a service. Please go
													through the conditions carefully and if you accept them,
													you may register yourself and transact on the site. On
													using this site for service delivery, you are deemed to
													have agreed to the terms and conditions set forth below. If
													You do not agree with all these terms and conditions, you
													must not transact on this Website.</p>
												<p>If a user violates the terms and conditions
													Government (service owner) reserves the right to deactivate
													all such user registration and cancel any or all services
													requested without any notice. Garbage / Junk values in
													profile may lead to Deactivation.</p>
												<p>Operationalization of this agreement is subject to
													existing laws and legal processes of the respective
													Government, and nothing contained in this agreement is in
													derogation of Government's right to comply with law
													enforcement requests or requirements relating to your use
													of this Web Site or information provided to or gathered by
													this site with respect to such use. You agree that
													Government may provide details of your use of the Web Site
													to regulators or police or to any other third party, or in
													order to resolve disputes or complaints which relate to the
													Web Site, at Governmentâs complete discretion.</p>
												<p>This agreement is made between: respective service
													owner department of the respective government who has
													configured the serviceGovernment ('Us') and The
													User ('You'), the individual, whose details are
													set out in the Portal User Creation page.</p>
												<strong>Payment Option
													<p></p>
												</strong>
												<p>The list of payment options available are internet
													banking /debit card payment / credit card payment from
													banks that are listed when selecting each of the above
													options. Apart from the fee chargeable to Government
													against each service, bank / payment gateway transaction
													charges will be applicable extra. In case of a failed
													transaction the user shall have no right to claim the
													amount. The loss on this account shall not be borne either
													by Government or by the Banks /Payment Gateways.</p>
												<p>
													<strong>User Creation</strong>
												</p>
												<p>You are responsible for maintaining the
													confidentiality of the password and account, and are fully
													responsible for all activities that occur under your
													password or account. Complaints Procedure</p>
												<p>You can reach us on the contact details given in the
													'Contacts' option given in the login page.</p>
												<p>Your obligations</p>
												<p>
													<strong>General Obligations:</strong>
												</p>
												<p>You shall access web site only for lawful
													purposes and you shall be responsible for complying with
													all applicable laws, statutes and regulations in connection
													with the use of Government web site. This Website is for
													your personal or commercial use by approved kiosks. You
													shall not modify, copy, distribute, transmit, display,
													perform, reproduce, publish, license, create derivative
													works from, transfer or sell any information, or services
													obtained from this Website. You shall not create a
													hypertext link to the Website or "frame" the
													Website, except with the express advance written permission
													of the Government.</p>
												<p>
													<strong>Information Provided</strong>
												</p>
												<p>The information you provide in the Registration page
													must be complete and accurate. Government 00. reserves the
													right at all times to disclose any information as deems
													necessary to satisfy any applicable law, regulation, legal
													process.</p>
												<p>
													<strong>Termination</strong>
												</p>
												<p>We may at any time at our sole discretion and without
													giving any reason or any prior notice terminate or
													temporarily suspend your access to all or any part of the
													web site.</p>
                </div>
            </div>
        </div>
    
		<div class="card">
            <div class="card-header p-0" id="headingFour">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link collapsed w-100 text-left" data-toggle="collapse" data-target="#collapseFour">
                    <i class="fa fa-plus  float-right "></i>Contact us</button>
                </h2>
            </div>
            <div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordionExample">
                <div class="card-body">
                <p>Email at <i class="fa fa-envelope"></i> <em>egramswaraj[at]gov[dot]in</em>
				</p><p>Ministry of Panchayai Raj<br>Government of India<br>
				11<sup>th</sup> Floor, J.P. Building,<br>
				Kasturba Gandhi Marg, Connaught Place,
				<br>New Delhi-110001</p>
				<p></p>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header p-0" id="headingFive">
                <h2 class="mb-0">
                    <button type="button" class="btn btn-link collapsed w-100 text-left" data-toggle="collapse" data-target="#collapseFive">
                    <i class="fa fa-plus  float-right "></i>Web Information Manager</button>
                </h2>
            </div>
            <div id="collapseFive" class="collapse" aria-labelledby="headingFive" data-parent="#accordionExample">
                <div class="card-body">
                <p>Shri Alok Prem Nagar<br>Joint Secretary<br><i class="fa fa-phone"></i> 011-23356556(O)<br>
                <i class="fa fa-envelope"></i> <em>ap[dot]nagar[at]gov[dot]in</em></p>
                </div>
            </div>
        </div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div></div>
	<style>
#quickModal .accordion .card-header .btn-link:not(.collapsed){
background-color:#f9e3a1;
}
#quickModal .card-body{
	min-height:150px;
	overflow-y:scroll;
	height:175px;
}

</style>
	<script>
	function allPolicies(id) {
		
		var a = "heading";
		var newid = a + id; 
		$(".card-header .btn").addClass("collapsed");
		$(".card-header .btn .fa").addClass("fa-plus").removeClass("fa-minus");
		$(".collapse").removeClass("show");
		$("#" + newid +"  .btn").removeClass("collapsed");
		$("#" + newid +"  .btn .fa").removeClass("fa-plus").addClass("fa-minus");
		$("#collapse"+id).addClass("show");
	}</script>

	
	
	
	
 <!-- #####################################Alert ############################### -->
 
 





 
 





 
 
  
   


'''
    str_res_bis = re.search(r'SECTION 2(.*)SECTION 3', str_res, flags=re.DOTALL)
    str_res_ter = re.search(r'<table.*</table>', str_res_bis.group(0), flags=re.DOTALL)
    assert str_res_ter is not None

def test_regex_1():
    str_res = '''
                             	<thead class="bg-dark text-white font10px">



                             		<tr>
    					<th colspan="4" width="50%" align="left">
    					Plan Year
    									: <strong> 2020-2021</strong>
    									&nbsp;&nbsp;&nbsp;&nbsp;
    						State			
    									  : <strong> MAHARASHTRA </strong>
    							</th>

                             		</tr>
                             		<tr>
                             		                         		<td class="text-center">S.No.</td>
    							<td class="text-center">District Panchayat &amp; equivalent</td>
    							<td class="text-center">Block Panchayat &amp; equivalent</td>
    							<td class="text-center">Total Approved plan count</td>
    						     </tr>

    						     	</thead><tbody>





    	                         	<tr>
    	                         		<td class="text-center">1</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">AKOLE</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4635',0);">146</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">2</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">JAMKHED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4636',0);">58</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">3</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">KARJAT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4637',0);">91</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">4</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">KOPARGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4638',0);">75</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">5</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">NAGAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4639',0);">105</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">6</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">NEVASA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4640',0);">114</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">7</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">PARNER</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4641',0);">114</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">8</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">PATHARDI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4642',0);">107</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">9</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">RAHATA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4643',0);">50</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">10</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">RAHURI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4644',0);">82</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">11</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">SANGAMNER</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4645',0);">142</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">12</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">SHEVGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4646',0);">94</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">13</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">SHRIGONDA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4647',0);">86</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">14</td>


    													<td class="text-center">AHMEDNAGAR</td>






    										 							<td class="text-center">SHRIRAMPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','424','4648',0);">52</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">15</td>


    													<td class="text-center">AKOLA</td>






    										 							<td class="text-center">AKOLA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','425','4649',0);">97</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">16</td>


    													<td class="text-center">AKOLA</td>






    										 							<td class="text-center">AKOT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','425','4650',0);">85</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">17</td>


    													<td class="text-center">AKOLA</td>






    										 							<td class="text-center">BALAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','425','4651',0);">66</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">18</td>


    													<td class="text-center">AKOLA</td>






    										 							<td class="text-center">BARSHITAKLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','425','4652',0);">82</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">19</td>


    													<td class="text-center">AKOLA</td>






    										 							<td class="text-center">MURTIJAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','425','4653',0);">86</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">20</td>


    													<td class="text-center">AKOLA</td>






    										 							<td class="text-center">PATUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','425','4654',0);">57</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">21</td>


    													<td class="text-center">AKOLA</td>






    										 							<td class="text-center">TELHARA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','425','4655',0);">62</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">22</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">ACHALPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4656',0);">70</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">23</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">AMRAVATI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4657',0);">59</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">24</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">ANJANGAON S</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4658',0);">49</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">25</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">BHATKULI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4659',0);">48</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">26</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">CHANDUR RIL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4660',0);">49</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">27</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">CHANDUR BZ</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4661',0);">67</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">28</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">CHIKHALDARA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4662',0);">54</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">29</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">DARYAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4663',0);">74</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">30</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">DHAMANGAON RIL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4664',0);">62</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">31</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">DHARNI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4665',0);">62</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">32</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">MORSHI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4666',0);">67</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">33</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">NANDGAON KH</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4667',0);">68</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">34</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">TIWSA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4668',0);">45</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">35</td>


    													<td class="text-center">AMRAVATI</td>






    										 							<td class="text-center">WARUD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','426','4669',0);">66</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">36</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">AURANGABAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4670',0);">114</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">37</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">GANGAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4671',0);">110</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">38</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">KANAND</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4672',0);">138</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">39</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">KHULTABAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4673',0);">39</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">40</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">PAITHAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4674',0);">108</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">41</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">PHULAMBRI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4675',0);">70</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">42</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">SILLOD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4676',0);">103</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">43</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">SOEGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4677',0);">46</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">44</td>


    													<td class="text-center">AURANGABAD</td>






    										 							<td class="text-center">VAIJAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','427','4678',0);">135</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">45</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">AMBAJOGAI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4679',0);">99</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">46</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">ASHTI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4680',0);">125</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">47</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">BEED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4681',0);">175</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">48</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">DHARUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4682',0);">54</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">49</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">GEORAI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4683',0);">137</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">50</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">KAIJ</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4684',0);">114</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">51</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">MAJALGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4685',0);">91</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">52</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">PARALI V .</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4686',0);">90</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">53</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">PATODA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4687',0);">59</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">54</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">SHIRUR ( KA )</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4688',0);">52</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">55</td>


    													<td class="text-center">BEED</td>






    										 							<td class="text-center">WADWANI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','428','4689',0);">35</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">56</td>


    													<td class="text-center">BHANDARA</td>






    										 							<td class="text-center">BHANDARA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','429','4690',0);">94</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">57</td>


    													<td class="text-center">BHANDARA</td>






    										 							<td class="text-center">LAKHANDUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','429','4691',0);">62</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">58</td>


    													<td class="text-center">BHANDARA</td>






    										 							<td class="text-center">LAKHANI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','429','4692',0);">71</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">59</td>


    													<td class="text-center">BHANDARA</td>






    										 							<td class="text-center">MOHADI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','429','4693',0);">76</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">60</td>


    													<td class="text-center">BHANDARA</td>






    										 							<td class="text-center">PAUNI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','429','4694',0);">79</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">61</td>


    													<td class="text-center">BHANDARA</td>






    										 							<td class="text-center">SAKOLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','429','4695',0);">62</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">62</td>


    													<td class="text-center">BHANDARA</td>






    										 							<td class="text-center">TUMSAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','429','4696',0);">97</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">63</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">BULDANA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4697',0);">66</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">64</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">CHIKHLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4698',0);">99</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">65</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">D. RAJA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4699',0);">48</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">66</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">JALGAONJAMOD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4700',0);">47</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">67</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">KHAMGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4701',0);">97</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">68</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">LONAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4702',0);">59</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">69</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">MALKAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4703',0);">49</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">70</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">MEHKAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4704',0);">98</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">71</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">MOTALA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4705',0);">65</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">72</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">NANDURA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4706',0);">65</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">73</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">SANGRAMPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4707',0);">50</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">74</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">SHEGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4708',0);">46</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">75</td>


    													<td class="text-center">BULDHANA</td>






    										 							<td class="text-center">SINDKHEDRAJA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','430','4709',0);">80</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">76</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">BALLARPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4710',0);">17</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">77</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">BHADRAWATI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4711',0);">70</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">78</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">BRAHMAPURI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4712',0);">75</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">79</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">CHANDRAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4713',0);">48</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">80</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">CHIMUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4714',0);">93</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">81</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">GONDPIPRI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4715',0);">50</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">82</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">JIWATI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4716',0);">36</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">83</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">KORPANA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4717',0);">52</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">84</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">MUL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4718',0);">49</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">85</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">NAGBHID</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4719',0);">56</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">86</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">POMBHURNA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4720',0);">31</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">87</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">RAJURA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4721',0);">65</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">88</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">SAOLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4722',0);">54</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">89</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">SINDEWAHI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4723',0);">51</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">90</td>


    													<td class="text-center">CHANDRAPUR</td>






    										 							<td class="text-center">WARORA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','431','4724',0);">81</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">91</td>


    													<td class="text-center">DHULE</td>






    										 							<td class="text-center">DHULE</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','432','4725',0);">131</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">92</td>


    													<td class="text-center">DHULE</td>






    										 							<td class="text-center">SAKRI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','432','4726',0);">169</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">93</td>


    													<td class="text-center">DHULE</td>






    										 							<td class="text-center">SHINDKHEDA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','432','4727',0);">123</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">94</td>


    													<td class="text-center">DHULE</td>






    										 							<td class="text-center">SHIRPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','432','4728',0);">118</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">95</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">AHERI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4729',0);">39</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">96</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">ARMORI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4730',0);">32</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">97</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">BHAMARAGAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4731',0);">19</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">98</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">CHAMORSHI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4732',0);">75</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">99</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">DESAIGANJ (WADSA)</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4733',0);">20</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">100</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">DHANORA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4734',0);">61</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">101</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">ETAPALLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4735',0);">31</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">102</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">GADCHIROLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4736',0);">51</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">103</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">KORCHI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4737',0);">29</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">104</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">KURKHEDA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4738',0);">45</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">105</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">MULCHERA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4739',0);">16</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">106</td>


    													<td class="text-center">GADCHIROLI</td>






    										 							<td class="text-center">SIRONCHA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','433','4740',0);">39</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">107</td>


    													<td class="text-center">GONDIA</td>






    										 							<td class="text-center">AMGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','434','4741',0);">57</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">108</td>


    													<td class="text-center">GONDIA</td>






    										 							<td class="text-center">ARJUNI MORGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','434','4742',0);">70</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">109</td>


    													<td class="text-center">GONDIA</td>






    										 							<td class="text-center">DEORI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','434','4743',0);">55</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">110</td>


    													<td class="text-center">GONDIA</td>






    										 							<td class="text-center">GONDIA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','434','4744',0);">109</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">111</td>


    													<td class="text-center">GONDIA</td>






    										 							<td class="text-center">GOREGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','434','4745',0);">55</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">112</td>


    													<td class="text-center">GONDIA</td>






    										 							<td class="text-center">SADAK ARJUNI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','434','4746',0);">63</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">113</td>


    													<td class="text-center">GONDIA</td>






    										 							<td class="text-center">SALEKASA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','434','4747',0);">41</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">114</td>


    													<td class="text-center">GONDIA</td>






    										 							<td class="text-center">TIRORA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','434','4748',0);">95</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">115</td>


    													<td class="text-center">HINGOLI</td>






    										 							<td class="text-center">AUNDHA NAGNATH</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','435','4749',0);">101</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">116</td>


    													<td class="text-center">HINGOLI</td>






    										 							<td class="text-center">BASMAT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','435','4750',0);">119</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">117</td>


    													<td class="text-center">HINGOLI</td>






    										 							<td class="text-center">HINGOLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','435','4751',0);">111</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">118</td>


    													<td class="text-center">HINGOLI</td>






    										 							<td class="text-center">KALAMNURI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','435','4752',0);">125</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">119</td>


    													<td class="text-center">HINGOLI</td>






    										 							<td class="text-center">SENGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','435','4753',0);">107</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">120</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">AMALNER</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4754',0);">119</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">121</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">BHADGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4755',0);">49</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">122</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">BHUSAWAL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4756',0);">39</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">123</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">BODWAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4757',0);">38</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">124</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">CHALISGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4758',0);">108</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">125</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">CHOPDA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4759',0);">90</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">126</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">DHARANGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4760',0);">74</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">127</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">ERANDOL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4761',0);">52</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">128</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">JALGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4762',0);">70</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">129</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">JAMNER</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4763',0);">106</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">130</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">MUKTAINAGAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4764',0);">61</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">131</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">PACHORA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4765',0);">100</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">132</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">PAROLA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4766',0);">83</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">133</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">RAVER</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4767',0);">95</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">134</td>


    													<td class="text-center">JALGAON</td>






    										 							<td class="text-center">YAWAL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','436','4768',0);">67</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">135</td>


    													<td class="text-center">JALNA</td>






    										 							<td class="text-center">AMBAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','437','4769',0);">111</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">136</td>


    													<td class="text-center">JALNA</td>






    										 							<td class="text-center">BADNAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','437','4770',0);">79</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">137</td>


    													<td class="text-center">JALNA</td>






    										 							<td class="text-center">BHOKARDAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','437','4771',0);">124</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">138</td>


    													<td class="text-center">JALNA</td>






    										 							<td class="text-center">GHANSAWANGI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','437','4772',0);">97</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">139</td>


    													<td class="text-center">JALNA</td>






    										 							<td class="text-center">JAFRABAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','437','4773',0);">72</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">140</td>


    													<td class="text-center">JALNA</td>






    										 							<td class="text-center">JALNA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','437','4774',0);">123</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">141</td>


    													<td class="text-center">JALNA</td>






    										 							<td class="text-center">MANTHA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','437','4775',0);">92</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">142</td>


    													<td class="text-center">JALNA</td>






    										 							<td class="text-center">PARTUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','437','4776',0);">81</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">143</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">AJARA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4777',0);">73</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">144</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">GAGAN BAVADA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4778',0);">29</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">145</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">BHUDARGAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4779',0);">97</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">146</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">CHANDGAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4780',0);">109</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">147</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">GADHINGLAJ</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4781',0);">89</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">148</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">HATKANANGALE</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4782',0);">60</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">149</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">KAGAL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4783',0);">83</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">150</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">KARVEER</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4784',0);">118</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">151</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">PANHALA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4785',0);">111</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">152</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">RADHANAGARI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4786',0);">98</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">153</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">SHAHUWADI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4787',0);">106</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">154</td>


    													<td class="text-center">KOLHAPUR</td>






    										 							<td class="text-center">SHIROL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','438','4788',0);">52</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">155</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">AHEMADPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4789',0);">97</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">156</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">AUSA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4790',0);">109</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">157</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">CHAKUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4791',0);">71</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">158</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">DEONI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4792',0);">45</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">159</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">JALKOT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4793',0);">43</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">160</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">LATUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4794',0);">110</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">161</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">NILANGA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4795',0);">116</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">162</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">RENAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4796',0);">65</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">163</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">SHIRUR ANANTPAL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4797',0);">42</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">164</td>


    													<td class="text-center">LATUR</td>






    										 							<td class="text-center">UDGIR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','439','4798',0);">87</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">165</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">BHIVAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4799',0);">56</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">166</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">HINGNA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4800',0);">53</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">167</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">KALMESHWAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4801',0);">50</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">168</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">KAMPTEE</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4802',0);">47</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">169</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">KATOL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4803',0);">83</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">170</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">KUHI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4804',0);">59</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">171</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">MOUDA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4805',0);">63</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">172</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">NAGPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4806',0);">66</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">173</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">NARKHED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4807',0);">70</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">174</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">PARSEONI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4808',0);">51</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">175</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">RAMTEK</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4809',0);">48</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">176</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">SAONER</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4810',0);">75</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">177</td>


    													<td class="text-center">NAGPUR</td>






    										 							<td class="text-center">UMRED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','440','4811',0);">47</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">178</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">ARDHAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4812',0);">39</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">179</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">BHOKAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4813',0);">66</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">180</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">BILOLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4814',0);">73</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">181</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">DEGLUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4815',0);">90</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">182</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">DHARMABAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4816',0);">45</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">183</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">HADGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4817',0);">125</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">184</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">HIMAYATNAGAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4818',0);">52</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">185</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">KANDHAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4819',0);">116</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">186</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">KINWAT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4820',0);">134</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">187</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">LOHA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4821',0);">118</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">188</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">MAHUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4822',0);">62</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">189</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">MODKHED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4823',0);">50</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">190</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">MOKHED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4824',0);">128</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">191</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">NAIGAON (KH)</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4825',0);">80</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">192</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">NANDED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4826',0);">73</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">193</td>


    													<td class="text-center">NANDED</td>






    										 							<td class="text-center">UMRI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','441','4827',0);">57</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">194</td>


    													<td class="text-center">NANDURBAR</td>






    										 							<td class="text-center">AKKALKUWA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','442','4828',0);">77</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">195</td>


    													<td class="text-center">NANDURBAR</td>






    										 							<td class="text-center">AKARANI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','442','4829',0);">50</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">196</td>


    													<td class="text-center">NANDURBAR</td>






    										 							<td class="text-center">NANDURBAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','442','4830',0);">137</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">197</td>


    													<td class="text-center">NANDURBAR</td>






    										 							<td class="text-center">NAVAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','442','4831',0);">114</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">198</td>


    													<td class="text-center">NANDURBAR</td>






    										 							<td class="text-center">SHAHADA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','442','4832',0);">150</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">199</td>


    													<td class="text-center">NANDURBAR</td>






    										 							<td class="text-center">TALODA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','442','4833',0);">67</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">200</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">BAGLAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4834',0);">131</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">201</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">CHANDWAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4835',0);">90</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">202</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">DEOLA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4836',0);">42</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">203</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">DINDORI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4837',0);">121</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">204</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">IGATPURI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4838',0);">96</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">205</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">KALWAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4839',0);">86</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">206</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">MALEGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4840',0);">125</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">207</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">NANDGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4841',0);">88</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">208</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">NASHIK</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4842',0);">66</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">209</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">NIPHAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4843',0);">119</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">210</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">PETH</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4844',0);">73</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">211</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">SINNAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4845',0);">114</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">212</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">SURGANA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4846',0);">61</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">213</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">TRIMBAK</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4847',0);">84</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">214</td>


    													<td class="text-center">NASHIK</td>






    										 							<td class="text-center">YEOLA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','443','4848',0);">89</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">215</td>


    													<td class="text-center">OSMANABAD</td>






    										 							<td class="text-center">BHOOM</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','444','4849',0);">74</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">216</td>


    													<td class="text-center">OSMANABAD</td>






    										 							<td class="text-center">KALAMB</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','444','4850',0);">91</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">217</td>


    													<td class="text-center">OSMANABAD</td>






    										 							<td class="text-center">LOHARA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','444','4851',0);">44</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">218</td>


    													<td class="text-center">OSMANABAD</td>






    										 							<td class="text-center">OMERGA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','444','4852',0);">80</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">219</td>


    													<td class="text-center">OSMANABAD</td>






    										 							<td class="text-center">OSMANABAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','444','4853',0);">111</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">220</td>


    													<td class="text-center">OSMANABAD</td>






    										 							<td class="text-center">PARANDA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','444','4854',0);">72</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">221</td>


    													<td class="text-center">OSMANABAD</td>






    										 							<td class="text-center">TULJAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','444','4855',0);">108</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">222</td>


    													<td class="text-center">OSMANABAD</td>






    										 							<td class="text-center">WASHI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','444','4856',0);">42</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">223</td>


    													<td class="text-center">PALGHAR</td>






    										 							<td class="text-center">DAHANU</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','261449','4946',0);">85</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">224</td>


    													<td class="text-center">PALGHAR</td>






    										 							<td class="text-center">JAWHAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','261449','4947',0);">50</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">225</td>


    													<td class="text-center">PALGHAR</td>






    										 							<td class="text-center">MOKHADA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','261449','4949',0);">27</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">226</td>


    													<td class="text-center">PALGHAR</td>






    										 							<td class="text-center">PALGHAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','261449','4951',0);">133</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">227</td>


    													<td class="text-center">PALGHAR</td>






    										 							<td class="text-center">TALASARI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','261449','4953',0);">21</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">228</td>


    													<td class="text-center">PALGHAR</td>






    										 							<td class="text-center">VASAI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','261449','4954',0);">31</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">229</td>


    													<td class="text-center">PALGHAR</td>






    										 							<td class="text-center">VIKRAMGAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','261449','4955',0);">42</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">230</td>


    													<td class="text-center">PALGHAR</td>






    										 							<td class="text-center">WADA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','261449','4956',0);">84</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">231</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">GANGAKHED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4857',0);">84</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">232</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">JINTUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4858',0);">136</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">233</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">MANWAT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4859',0);">49</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">234</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">PALAM</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4860',0);">66</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">235</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">PARBHANI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4861',0);">117</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">236</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">PATHRI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4862',0);">49</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">237</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">PURNA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4863',0);">79</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">238</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">SAILU</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4864',0);">82</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">239</td>


    													<td class="text-center">PARBHANI</td>






    										 							<td class="text-center">SONPETH</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','445','4865',0);">42</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">240</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">AMBEGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4866',0);">103</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">241</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">BARAMATI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4867',0);">99</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">242</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">BHOR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4868',0);">155</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">243</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">DAUND</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4869',0);">80</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">244</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">HAVELI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4870',0);">89</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">245</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">INDAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4871',0);">115</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">246</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">JUNNAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4872',0);">142</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">247</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">KHED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4873',0);">162</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">248</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">MAVAL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4874',0);">103</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">249</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">MULSHI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4875',0);">95</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">250</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">PURANDAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4877',0);">93</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">251</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">SHIRUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4878',0);">93</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">252</td>


    													<td class="text-center">PUNE</td>






    										 							<td class="text-center">VELHE</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','446','4879',0);">71</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">253</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">ALIBAG</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4880',0);">62</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">254</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">KARJAT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4881',0);">54</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">255</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">KHALAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4882',0);">44</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">256</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">MAHAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4883',0);">134</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">257</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">MANGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4884',0);">74</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">258</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">MHASALA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4885',0);">39</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">259</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">MURUD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4886',0);">24</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">260</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">PANVEL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4887',0);">71</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">261</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">PEN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4888',0);">65</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">262</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">POLADPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4889',0);">42</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">263</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">ROHA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4890',0);">64</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">264</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">SHRIVARDHAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4891',0);">43</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">265</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">SUDHAGAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4892',0);">34</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">266</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">TALA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4893',0);">25</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">267</td>


    													<td class="text-center">RAIGAD</td>






    										 							<td class="text-center">URAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','447','4894',0);">35</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">268</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">CHIPALUN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4895',0);">130</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">269</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">DAPOLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4896',0);">106</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">270</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">GUHAGAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4897',0);">66</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">271</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">KHED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4898',0);">114</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">272</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">LANJA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4899',0);">60</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">273</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">MANDANGAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4900',0);">49</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">274</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">RAJAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4901',0);">101</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">275</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">RATNAGIRI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4902',0);">94</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">276</td>


    													<td class="text-center">RATNAGIRI</td>






    										 							<td class="text-center">SANGMESHWAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','448','4903',0);">126</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">277</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">ATPADI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4904',0);">56</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">278</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">JATH</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4905',0);">116</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">279</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">KADEGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4906',0);">54</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">280</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">KAVATHEMAHANKAL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4907',0);">59</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">281</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">KHANAPUR-VITA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4908',0);">64</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">282</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">MIRAJ</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4909',0);">64</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">283</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">PALUS</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4910',0);">33</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">284</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">SHIRALA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4911',0);">91</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">285</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">TASGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4912',0);">68</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">286</td>


    													<td class="text-center">SANGLI</td>






    										 							<td class="text-center">VALVA-ISLAMPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','449','4913',0);">94</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">287</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">JAWALI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4914',0);">125</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">288</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">KARAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4915',0);">200</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">289</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">KHANDALA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4916',0);">63</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">290</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">KHATAV</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4917',0);">133</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">291</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">KOREGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4918',0);">142</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">292</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">MAHABALESHWAR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4919',0);">79</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">293</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">MAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4920',0);">95</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">294</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">PATAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4921',0);">238</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">295</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">PHALTAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4922',0);">128</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">296</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">SATARA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4923',0);">194</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">297</td>


    													<td class="text-center">SATARA</td>






    										 							<td class="text-center">WAI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','450','4924',0);">99</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">298</td>


    													<td class="text-center">SINDHUDURG</td>






    										 							<td class="text-center">DEOGAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','451','4925',0);">72</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">299</td>


    													<td class="text-center">SINDHUDURG</td>






    										 							<td class="text-center">DODAMARG</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','451','4926',0);">36</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">300</td>


    													<td class="text-center">SINDHUDURG</td>






    										 							<td class="text-center">KANKAVALI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','451','4927',0);">63</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">301</td>


    													<td class="text-center">SINDHUDURG</td>






    										 							<td class="text-center">KUDAL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','451','4928',0);">68</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">302</td>


    													<td class="text-center">SINDHUDURG</td>






    										 							<td class="text-center">MALVAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','451','4929',0);">65</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">303</td>


    													<td class="text-center">SINDHUDURG</td>






    										 							<td class="text-center">SAWANTWADI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','451','4930',0);">63</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">304</td>


    													<td class="text-center">SINDHUDURG</td>






    										 							<td class="text-center">VAIBHAVAWADI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','451','4931',0);">34</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">305</td>


    													<td class="text-center">SINDHUDURG</td>






    										 							<td class="text-center">VENGURLA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','451','4932',0);">30</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">306</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">AKKALKOT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4933',0);">117</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">307</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">BARSHI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4934',0);">129</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">308</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">KARMALA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4935',0);">105</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">309</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">MADHA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4936',0);">108</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">310</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">MALSHIRAS</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4937',0);">107</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">311</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">MANGALVEDHE</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4938',0);">79</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">312</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">MOHOL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4939',0);">94</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">313</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">PANDHARPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4940',0);">94</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">314</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">SANGOLA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4941',0);">76</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">315</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">SOLAPUR NORTH</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4942',0);">36</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">316</td>


    													<td class="text-center">SOLAPUR</td>






    										 							<td class="text-center">SOUTH SOLAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','452','4943',0);">83</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">317</td>


    													<td class="text-center">THANE</td>






    										 							<td class="text-center">AMBERNATH</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','453','4944',0);">28</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">318</td>


    													<td class="text-center">THANE</td>






    										 							<td class="text-center">BHIWANDI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','453','4945',0);">120</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">319</td>


    													<td class="text-center">THANE</td>






    										 							<td class="text-center">KALYAN</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','453','4948',0);">46</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">320</td>


    													<td class="text-center">THANE</td>






    										 							<td class="text-center">MURBAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','453','4950',0);">126</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">321</td>


    													<td class="text-center">THANE</td>






    										 							<td class="text-center">SHAHAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','453','4952',0);">110</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">322</td>


    													<td class="text-center">WARDHA</td>






    										 							<td class="text-center">ARVI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','454','4957',0);">72</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">323</td>


    													<td class="text-center">WARDHA</td>






    										 							<td class="text-center">ASHTI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','454','4958',0);">41</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">324</td>


    													<td class="text-center">WARDHA</td>






    										 							<td class="text-center">DEOLI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','454','4959',0);">63</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">325</td>


    													<td class="text-center">WARDHA</td>






    										 							<td class="text-center">HINGANGHAT</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','454','4960',0);">76</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">326</td>


    													<td class="text-center">WARDHA</td>






    										 							<td class="text-center">KARANJA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','454','4961',0);">59</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">327</td>


    													<td class="text-center">WARDHA</td>






    										 							<td class="text-center">SAMUDRAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','454','4962',0);">71</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">328</td>


    													<td class="text-center">WARDHA</td>






    										 							<td class="text-center">SELOO</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','454','4963',0);">62</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">329</td>


    													<td class="text-center">WARDHA</td>






    										 							<td class="text-center">WARDHA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','454','4964',0);">76</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">330</td>


    													<td class="text-center">WASHIM</td>






    										 							<td class="text-center">KARANJA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','455','4965',0);">91</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">331</td>


    													<td class="text-center">WASHIM</td>






    										 							<td class="text-center">MALEGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','455','4966',0);">83</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">332</td>


    													<td class="text-center">WASHIM</td>






    										 							<td class="text-center">MANGRULPIR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','455','4967',0);">76</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">333</td>


    													<td class="text-center">WASHIM</td>






    										 							<td class="text-center">MANORA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','455','4968',0);">77</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">334</td>


    													<td class="text-center">WASHIM</td>






    										 							<td class="text-center">RISOD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','455','4969',0);">80</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">335</td>


    													<td class="text-center">WASHIM</td>






    										 							<td class="text-center">WASHIM</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','455','4970',0);">84</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">336</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">ARNI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4971',0);">77</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">337</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">BABHULGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4972',0);">65</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">338</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">DARWHA</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4973',0);">86</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">339</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">DIGRAS</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4974',0);">55</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">340</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">GHATANJI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4975',0);">71</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">341</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">KALAMB</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4976',0);">61</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">342</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">KELAPUR</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4977',0);">74</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">343</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">MAHAGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4978',0);">76</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">344</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">MAREGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4979',0);">56</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">345</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">NER</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4980',0);">51</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">346</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">PUSAD</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4981',0);">120</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">347</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">RALEGAON</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4982',0);">73</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">348</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">UMARKHED</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4983',0);">92</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">349</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">WANI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4984',0);">101</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">350</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">YAVATMAL</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4985',0);">88</a></td>






    								</tr>


    	                         	<tr>
    	                         		<td class="text-center">351</td>


    													<td class="text-center">YAVATMAL</td>






    										 							<td class="text-center">ZARI JAMNI</td>	







    											<td class="text-center"><a href="#" class="level-link" onclick="javascript:getgpreport('27',3,'2020','456','4986',0);">55</a></td>






    								</tr>



                             	</tbody>






                             	'''
    state_code = 27
    financial_year = 2020
    district_block_panch_tuples = re.findall(
        rf"<td class=\"text-center\">([A-Za-z- ().]+)</td>[ \t\n]*<td class=\"text-center\">([A-Za-z- ().]+)</td>[ \t\n]*<td class=\"text-center\"><a href=\"#\" class=\"level-link\" onclick=\"javascript:getgpreport\('{state_code}',3,'{financial_year}','([0-9]+)','([0-9]+)',0\);\"",
        str_res)
    print(len(district_block_panch_tuples))


def test_regex_2():
    str_res = '''
        <tr>
                         	<td class="text-center">1</td>
                         	 
				 
							<td class="text-center">AHMEDNAGAR</td>
				 
				 
				 
				
								 
				 
				 							<td class="text-center">JAMKHED</td>	
				 
				 
				 
				
				 
				 
          <td class="text-center">AGHEE</td>	
           <td class="text-center">167702</td>				 
				 
				 
				
									 	
			<td class="text-center">2644199(Main Plan) </td>
								
							<td class="text-center"><a href="#" class="level-link" onclick="javascript:getplanView('2644199','167702',5,4,'AHMEDNAGAR','JAMKHED','AGHEE','3');"> View</a></td>
					</tr>
        '''
    panch_tuples = re.findall(
        rf"<td class=\"text-center\">([0-9_A-Za-z- ()\[\]./]+)</td>[ \t\n]*<td class=\"text-center\">([0-9]+)</td>[ \t\n]*<td class=\"text-center\">[0-9]+\((Main|Supplementary) Plan\)[ \t\n]*</td>[ \t\n]*<td class=\"text-center\"><a href=\"#\" class=\"level-link\" onclick=\"javascript:(getplanView\('([0-9]+)','([0-9]+)',([0-9]+),([0-9]+),'([A-Z ]+)','([A-Z ]+)','([A-Z ]+)','([0-9]+)'\);)\"",
        str_res)
    print(len(panch_tuples))


def test_regex_3():
    table_str = '''<tbody>



	
	
	
	
	
	









<tr>
<th align="left" width="2%">1</th>
<th align="left" width="48%">
	Drinking water
</th>



	
	
	
	
	
	
	
	
	


<td align="right">0</td>
<td align="right">0</td>
<td align="right">300000</td>
<td align="right">300000</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
						



			
</tr>





<tr>
<th align="left" width="2%">2</th>
<th align="left" width="48%">
	Education
</th>



	
	
	
	
	
	
	
	
	


<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">75000</td>
<td align="right">75000</td>
						



			
</tr>





<tr>
<th align="left" width="2%">3</th>
<th align="left" width="48%">
	Others
</th>



	
	
	
	
	
	
	
	
	


<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">80000</td>
<td align="right">80000</td>
						



			
</tr>





<tr>
<th align="left" width="2%">4</th>
<th align="left" width="48%">
	Roads
</th>



	
	
	
	
	
	
	
	
	


<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">650000</td>
<td align="right">650000</td>
						



			
</tr>





<tr>
<th align="left" width="2%">5</th>
<th align="left" width="48%">
	Rural electrification
</th>



	
	
	
	
	
	
	
	
	


<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">100000</td>
<td align="right">100000</td>
						



			
</tr>





<tr>
<th align="left" width="2%">6</th>
<th align="left" width="48%">
	Sanitation
</th>



	
	
	
	
	
	
	
	
	


<td align="right">0</td>
<td align="right">0</td>
<td align="right">150000</td>
<td align="right">150000</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
						



			
</tr>





<tr>
<th align="left" width="2%">7</th>
<th align="left" width="48%">
	Water Conservation
</th>



	
	
	
	
	
	
	
	
	


<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">700000</td>
<td align="right">700000</td>
						



			
</tr>


<tr>

<td align="left" width="2%"></td>
<td align="left" width="48%">
	<strong>Total</strong>
</td>




<td align="right">0</td>
<td align="right">0</td>
<td align="right">450000</td>
<td align="right">450000</td>

<td align="right">0</td>
<td align="right">0</td>
<td align="right">1605000</td>
<td align="right">1605000</td>
</tr>
</tbody>
'''
    table_str = table_str.replace('<tbody>', '<table>')
    table_str = table_str.replace('</tbody>', '</table>')
    table_str = table_str.replace('\t', '')
    table_str = table_str.replace('\n', '')
    table = etree.HTML(table_str).find('body/table')
    rows = iter(table)
    for row in rows:
        values = [col.text for col in row]
        print(values)


def test_regex_4():
    str_res = '''
								
							<td class="text-center"><a href="#" class="level-link" onclick="javascript:getplanView('2615314','27882',5,4,'AMBALA','AMBALA-I','UGARA','3');"> View</a></td>
					</tr>
							
                         	<tr>
                         	<td class="text-center">101</td>
                         	 
				 
							<td class="text-center">AMBALA</td>
				 
				 
				 
				
								 
				 
				 							<td class="text-center">AMBALA-I</td>	
				 
				 
				 
				
				 
				 
          <td class="text-center">RAWALON</td>	
           <td class="text-center">245736</td>				 
				 
				 
				
									 	
			<td class="text-center">2622802(Main Plan) </td>
								
							<td class="text-center"><a href="#" class="level-link" onclick="javascript:getplanView('2622802','245736',5,4,'AMBALA','AMBALA-I','RAWALON','3');"> View</a></td>
					</tr>
							
				
                         	</tbody>
                '''
    panch_tuples = re.findall(
        rf"<td class=\"text-center\">([0-9_A-Za-z- ()\[\]./]+)</td>[ \t\n]*<td class=\"text-center\">([0-9]+)</td>[ \t\n]*<td class=\"text-center\">[0-9]+\((Main|Supplementary) Plan\)[ \t\n]*</td>[ \t\n]*<td class=\"text-center\"><a href=\"#\" class=\"level-link\" onclick=\"javascript:(getplanView\('([0-9]+)','([0-9]+)',([0-9]+),([0-9]+),'([0-9_A-Za-z- ()\[\]./]+)','([0-9_A-Za-z- ()\[\]./]+)','([0-9_A-Za-z- ()\[\]./]+)','([0-9]+)'\);)\"",
        str_res)
    print(len(panch_tuples))
