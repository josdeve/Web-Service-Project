from flask import Flask, render_template_string, request, send_file
from flask import redirect, url_for
import pandas as pd
import io
from flask import flash
from flask import Flask, render_template_string, request, redirect, url_for, flash, session


app = Flask(__name__)
app.secret_key = '000'
users = {
    'user1': '010',
    'user2': '020',
    'user3': '030'
    
}
data = None

@app.before_request
def require_login():
    if request.endpoint != 'login' and 'username' not in session:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')

    return '''
<html>
<head>
    <title>Login</title>
    <style>
        body {
            background-image: url("                    ");
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
        }

        .login-container {
            display: flex;
            display: flex;
            background-color: #fff;
            border-radius: 34px;
            padding: 88px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            text-align: center;
            flex-direction: column;
            align-items: center;
        }

        .logo {
               width: 157px;
        height: 117px;
        margin-right: 4px;
        }

        h2 {
            margin-bottom: 20px;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 10px;
            color: #555;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 5px;
            border-radius: 30px;
            border: 0px solid #bbb;
            box-sizing: border-box;
            font-size: 16px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background-color: #45a049;
        }

        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <img class="logo" src="                   " alt="Logo">
        <div>
            <h2>Login</h2>

            <form method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br><br>
                <button type="submit">Login</button>
            </form>
        </div>
    </div>
</body>
</html>
'''


@app.route('/')

def home():
    global data
    if data is None:
        # Read the Excel file
        data = pd.read_excel('')
        # Remove the "HH:MM:SS" portion from Start Date and End Date columns
        data['Start Date'] = pd.to_datetime(data['Start Date']).dt.date
        data['End Date'] = pd.to_datetime(data['End Date']).dt.date
        return f""
 
    # Get the column names
    columns = data.columns.tolist()
    # Get unique values for Service Type and Contract Type columns
    service_types = data['Service Type'].unique().tolist()
    contract_types = data['Contract Type'].unique().tolist()
    Status = data['Status'].unique().tolist()
    # Get unique values for Start Date and End Date columns
    start_dates = data['Start Date'].unique().tolist()
    end_dates = data['End Date'].unique().tolist()
    # HTML template
    template = '''

  <!DOCTYPE html>
<html>
<head>
  <title>Data Display</title>
  <style>
    body {
      background-image: url("           ");
      font-family: Arial, sans-serif;
      color: #ffffff;
    }

    .header {
      display: flex;
      justify-content: center;
      background-image: url("            ");
      padding: 50px;
      box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }

    .logo {
      width: 150px;
      height: 120px;
      display: flex;
      justify-content: center;
      background-color: #ffffff;
      padding: 20px;
      box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }

    table {
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 20px;
      background-color: #1e90ff;
    }

    th,
    td {
      border: 1px solid black;
      padding: 8px;
      color: black ;
    }

    th {
      background-color: #1e90ff;
      color: black;
    }

    td {
      background-color: white;
    }

    select,
    input[type="date"] {
      width: 150px;
      padding: 8px;
      border: none;
      border-radius: 4px;
      background-color: #ffffff;
      color: #292929;
    }

    .dropdown {
      position: relative;
      display: inline-block;
    }

    .dropdown-content {
      display: none;
      position: absolute;
      background-color: #292929;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
      z-index: 1;
    }

    .dropdown-content a {
      color: #ffffff;
      padding: 12px 16px;
      text-decoration: none;
      display: block;
    }

    .dropdown:hover .dropdown-content {
      display: block;
    }

    h1 {
      text-align: center;
      color: #0089ffbd;;
          margin-top: -24px;
       
    }



    .filter-labels {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
      margin-bottom: 20px;
    }

    .filter-labels label {
      margin-right: 10px;
      color: #ffffff;
    }

    .data-container {
      display: flex;
      justify-content: center;
      background-color: #292929;
      padding: 20px;
    }

    .actions-dropdown {
      position: relative;
      display: inline-block;
    }
    

    .actions-dropdown button {
      background-color: #1e90ff;
      color: #ffffff;
      border: none;
      padding: 8px 16px;
      border-radius: 4px;
      cursor: pointer;
    }

    .actions-dropdown-content {
      display: none;
      position: absolute;
      background-color: #292929;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
      z-index: 1;
    }

    .actions-dropdown-content a {
      color: #ffffff;
      padding: 12px 16px;
      text-decoration: none;
      display: block;
    }

    .actions-dropdown:hover .actions-dropdown-content {
      display: block;
    }
   form {
            max-width: 350px;
    margin-right: px;
    background-color: #f2f2f2;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    position: relative;
    right: 0px;
    border: px solid #ffffff;
    text-align: center;
}
  }

  h2 {
    text-align: center;
    margin-bottom: 20px;
  }

  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: black;
    
  }
  select,input[type="date"] {
    width: 50%;
    padding: 3px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    text-align: center;
    
  }
  
  input[type="text"],
  
  input[type="date"] {
        width: 60%;
    padding: 3px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    text-align: center;
  }

  button[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }

  button[type="submit"]:hover {
    background-color: #45a049;
  }
  
        /* Cool styles */
    body {
      background-color: #f2f2f2;
      font-family: Arial, sans-serif;
    }

    .form-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .form-group {
      background-color: #fff;
      border-radius: 5px;
      padding: 15px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
      text-align: center;
      width: 300px;
   
      flex-direction: column;
        
 
    background-color: #f2f2f2;
    padding: 20px;
 
    right: 600px;
    top: 100px;
    position: ;
   
    margin-bottom: 92px;
    margin-left: 472px;

    }

    label {
      font-weight: bold;
      color: #333;
      margin-right: 10px;
    }

    select,
    input[type="date"] {
          width: 61%;
      padding: 3px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
    }

    select {
      background-color: #fff;
      color: #555;
    }

    input[type="date"] {
      background-color: #fff;
      color: #555;
      width: 180px;
    }
  
  
</style>
  </style>
</head>
<body>


  <form action="{{ url_for('logout') }}" method="get" style="position: absolute; top: 20px; right: 20px;">
    <button type="submit" style="padding: 5px 5px; font-size: 12px;">Logout</button>
  </form>
   </form>

  <div class="export-button" style="position: absolute; top: 20px; left: 20px;">
    <form action="{{ url_for('export_data') }}" method="get">
      <button type="submit" style="padding: 5px 5px; font-size: 12px;">Export Data</button>
    </form>
  </div>
</body>

          <div class="header">
    <img class="logo" src="                          " alt="Logo" >
  </div>
  <h1>  </h1>
  <h1></h1>
  
   
  <h2></h2>   
  <div style="
    width: 50% !important;
    float: left;">
    
<form action="{{ url_for('add_row') }}" method="POST">
  <div class="form-row">
  <label for="">[ ADD NEW DATA ]</label>
    <br>
    <label for="Project">Project</label>
    <input type="text" id="Project" name="Project" required>
  </div>
  <div class="form-row">
    <label for="service-type">Service Type</label>
    <input type="text" id="service-type" name="service_type" required>
  </div>
  <div class="form-row">
    <label for="contract-type">Contract Type</label>
    <select id="contract-type" name="contract_type" required>
    <option value="">-- Select the contract Type --</option>
      <option value="Multi year">Multi year</option>
      <option value="Single year">Single year</option>
      <option value="Blanked">Blanked</option>
      <option value="Agreement">Agreement</option>
    </select>
  </div>
  <div class="form-row">
    <label for="status">status</label>
    <select id="status" name="status" required>
    <option value="">-- Select the status --</option>
      <option value="RUN">RUN</option>
      <option value="STOP">STOP</option>
      <option value="HOLD">HOLD</option>
      <option value="NO STATUS">NO STATUS</option>
    </select>
  </div>
  <div class="form-row">
    <label for="start-date">Start Date</label>
    <input type="date" id="start-date" name="start_date" required min="2017-01-01">
  </div>
  <div class="form-row">
    <label for="end-date">End Date</label>
    <input type="date" id="end-date" name="end_date" required min="2017-01-01">
  </div>
  <br>
  <button type="submit">Add Row</button>
</form>
</div>
  <br><br>
  
  <div style="
    width: 50% !important;
    float: right;
">
  <div class="form-group">
   <label for="">[ SELECT THE TYPE ]</label>
    <br>
  <label for="service-type">Select Service Type</label>
  <select id="service-type" onchange="filterData('Service Type', this.value)">
    <option value="">All Service Types</option>
    {% for value in service_types %}
    <option value="{{ value }}">{{ value }}</option>
    {% endfor %}
  </select>



  <label for="contract-type">Select Contract Type</label>
  <select id="contract-type" onchange="filterData('Contract Type', this.value)">
    <option value="">All Contract Types</option>
    {% for value in contract_types %}
    <option value="{{ value }}">{{ value }}</option>
    {% endfor %}
  </select>



  <label for="Status">Select Status</label>
  <select id="Status" onchange="filterData('Status', this.value)">
    <option value="">All Statuses</option>
    {% for value in Status %}
    <option value="{{ value }}">{{ value }}</option>
    {% endfor %}
  </select>



  <label for="start-date">Select Start Date</label>
  <input type="date" id="start-date" onchange="filterData('Start Date', this.value)">



  <label for="end-date">Select End Date</label>
  <input type="date" id="end-date" onchange="filterData('End Date', this.value)">
</div>
</div>

<br class="clearfix">
    <br><br>  <br><br>
    
    <div style="background-image: url("              ");">
      
     
  <table id="data-table">
    <tr>
      {% for column in columns %}
        <th>{{ column }}</th>
      {% endfor %}
    </tr>
    {% for row in data.values %}
      <tr>
        {% for value in row %}
          <td>{{ value }}</td>
        {% endfor %}
        <td>
          <div class="dropdown">
            <button onclick="toggleDropdown(this)" class="dropbtn">Actions</button> <br>
            <div class="dropdown-content">
              <a href="{{ url_for('edit_row', index=loop.index0) }}">Edit</a>
              <a href="{{ url_for('remove_row', index=loop.index0) }}">Remove</a>
            </div>
          </div>
        </td>
      </tr>
    {% endfor %}
  </table>
     <script>
    function filterData(column, selectedValue) {
      var table = document.getElementById("data-table");
      var rows = table.getElementsByTagName("tr");
      // Iterate through each row
      for (var i = 1; i < rows.length; i++) {
        var row = rows[i];
        var rowData = row.getElementsByTagName("td");
        // Get data value of the selected column
        var rowValue = rowData[getColumnIndex(column)].innerText;
        // Check if the row should be displayed
        var displayRow = true;
        if (selectedValue && rowValue !== selectedValue) {
          displayRow = false;
        }
        // Update row display style
        row.style.display= displayRow ? "" : "none";
      }
    }
    
    

    function getColumnIndex(column) {
      var table = document.getElementById("data-table");
      var headersRow = table.rows[0];
      for (var i = 0; i < headersRow.cells.length; i++) {
        if (headersRow.cells[i].innerHTML === column) {
          return i;
        }
      }
      return -1;
    }
    function toggleDropdown(button) {
      var dropdownContent = button.nextElementSibling;
      dropdownContent.style.display = dropdownContent.style.display === "block" ? "none" : "block";
    }
  </script>
</body>  
</html>
'''
    return render_template_string(template, Status=Status, columns=columns, data=data, service_types=service_types, contract_types=contract_types, start_dates=start_dates, end_dates=end_dates)



@app.route('/edit_row/<int:index>', methods=['GET', 'POST'])
def edit_row(index):
    global data
    if request.method == 'POST':
        # Get the form data
        project = request.form['Project']
        service_type = request.form['service_type']
        contract_type = request.form['contract_type']
        start_date = pd.to_datetime(request.form['start_date']).date()
        end_date = pd.to_datetime(request.form['end_date']).date()
        No_of_Licenses = request.form['No_of_Licenses']
        Value = request.form['Value']
        status = request.form['status']
        Remarks = request.form['Remarks']
        start_date = pd.to_datetime(request.form['start_date']).date()
        end_date = pd.to_datetime(request.form['end_date']).date()
        # Update the row in the DataFrame
        data.loc[index, :] = [project, service_type, contract_type, start_date, end_date, No_of_Licenses, Value, status, Remarks]
        data.to_excel('                     ', index=False) #ENTER YOUR PATH 
        # Redirect back to the home page
        return redirect(url_for('home'))

    # Get the row data
    row = data.loc[index, :]
    # HTML template for editing a row
    template = '''
    <html>
<head>
  <title>Edit Row</title>
  <style>
    body {
      background-image: url("                  ");
      color: #ffffff;
      font-family: Arial, sans-serif;
    }
    
    .header {
      display: flex;
      justify-content: center;
      background-image: url("                         ");
      padding: 20px;
      box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .logo {
      width: 150px;
      height: 120px;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #ffffff;
      padding: 20px;
      box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    h2 {
      text-align: center;
      color: #ff9900;
    }
    
    form {
      margin: 0 auto;
      max-width: 500px;
    }
    
    label {
      display: block;
      margin-bottom: 10px;
      font-weight: bold;
          text-align: center;
    }
    
    input[type="text"],
    input[type="date"] {
      width: 100%;
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #dddddd;
      font-size: 14px;
    }
    
    button {
      background-color: #ff9900;
      color: #ffffff;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
      transition: background-color 0.3s ease;
      display: block;
      margin: 0 auto;
    }
    
    button:hover {
      background-color: #e68300;
    }
  </style>
</head>
<body>
  <div class="header">
    <img class="logo" src="                         " alt="Logo">
  </div>
  <h2>Edit Row</h2>
  <form action="{{ url_for('edit_row', index=index) }}" method="POST">
    <input type="hidden" name="index" value="{{ index }}">
    <label for="Project">Project</label>
    <input type="text" id="Project" name="Project" value="{{ row['Project'] }}" required>  <br />  <br />
    <label for="service-type">Service Type</label>
    <input type="text" id="service-type" name="service_type" value="{{ row['Service Type'] }}" required> <br /> <br />
    <label for="contract-type">Contract Type</label>
    <input type="text" id="contract-type" name="contract_type" value="{{ row['Contract Type'] }}" required>  <br /> <br />
    
    <label for="start-date">Start Date</label>
    <input type="date" id="start-date" name="start_date" value="{{ row['Start Date'] }}" required> <br /> <br />
    <label for="end-date">End Date</label>
    <input type="date" id="end-date" name="end_date" value="{{ row['End Date'] }}" required>  <br /> <br />
    <label for="No_of_Licenses">No of Licenses</label>
    <input type="text" name="No_of_Licenses" value="{{ row['No_of_Licenses'] }}">  <br /> <br />
    <label for="Value">Value</label>
    <input type="text" name="Value" value="{{ row['Value'] }}">  <br /> <br />
    <label for="status">Status</label>
    <input type="text" id="status" name="status" value="{{ row['Status'] }}" required>  <br /> <br />
    
    <label for="Remarks">Remarks</label>
    <input type="text" name="Remarks" value="{{ row['Remarks'] }}"> <br /> <br />
    <button type="submit">Save</button>
  </form>
</body>
</html>
    '''
    return render_template_string(template, index=index, row=row)


@app.route('/remove_row/<int:index>', methods=['GET', 'POST'])
def remove_row(index):
    if index in data.index:
        data.drop(index, inplace=True)
        data.reset_index(drop=True, inplace=True)
        data.to_excel('           ', index=False)
        flash('Row removed successfully!', 'success')
    else:
        flash('Invalid row index!', 'error')
    return redirect(url_for('home'))

@app.route('/add', methods=['POST'])
def add_row():
    global data

    # Get the form data
    Project = request.form['Project']
    service_type = request.form['service_type']
    contract_type = request.form['contract_type']
    status = request.form['status']
    start_date = pd.to_datetime(request.form['start_date']).date()
    end_date = pd.to_datetime(request.form['end_date']).date()

    # Create a new row
    new_row = pd.DataFrame({
        'Project':[Project],
        'Service Type': [service_type],
        'Contract Type': [contract_type],
        'Status': [status],
        'Start Date': [start_date],
        'End Date': [end_date]
    })

    # Append the new row to the data
    data = data.append(new_row, ignore_index=True)
    data.to_excel('     ', index=False)
    # Redirect back to the home page
    return redirect(url_for('home'))


@app.route('/export_data')
def export_data():
    global data
    if data is not None:
        # Export the data to a CSV file
        data.to_csv('exported_data.csv', index=False)
        return send_file('exported_data.csv', as_attachment=True)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
   
    app.run()