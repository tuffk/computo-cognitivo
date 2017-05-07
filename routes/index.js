exports.listSysTables = function(ibmdb,connString) {

	var d3 = require('d3');
	return function(req, res) {

	   	   
       ibmdb.open(connString, function(err, conn) {
			if (err ) {
			 res.send("error occurred " + err.message);
			}
			else {
				//conn.query("SELECT FIRST_NAME, LAST_NAME, EMAIL, WORK_PHONE from GOSALESHR.employee FETCH FIRST 10 ROWS ONLY", function(err, tables, moreResultSets) {
                conn.query("SELECT CUSTOMER, IS_FAILED from DASH11455.BDGMCLEAN", function(err, tables, moreResultSets) {


                    if ( !err ) {
					res.render('tablelist', {
						"tablelist" : tables,
						"tableName" : "10 rows from the GOSALESHR.EMPLOYEE table",
						"message": "Congratulations. Your connection to dashDB is successful."
						
					 });

					
				} else {
				   res.send("error occurred " + err.message);
				}

				/*
					Close the connection to the database
					param 1: The callback function to execute on completion of close function.
				*/
				conn.close(function(){
					console.log("Connection Closed");
					});
				});
			}
		} );
	   
	}
	}