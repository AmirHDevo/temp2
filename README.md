<table>
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Row 1, Cell 1</td>
    <td>Row 1, Cell 2</td>
  </tr>
</table>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tab Example</title>
    <style>
        /* Basic styling for the tabs */
        .tabs {
            display: flex;
            list-style: none;
            padding: 0;
        }

        .tab {
            margin-right: 10px;
            cursor: pointer;
            padding: 10px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 5px 5px 0 0;
        }

        .tab.active {
            background-color: #fff;
            border-bottom: 1px solid #fff;
        }

        /* Content area styling */
        .tab-content {
            display: none;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 0 0 5px 5px;
        }

        .tab-content.active {
            display: block;
        }
    </style>
</head>
<body>

<ul class="tabs">
    <li class="tab active" onclick="showTab('home')">Home</li>
    <li class="tab" onclick="showTab('product')">Product</li>
    <li class="tab" onclick="showTab('contacts')">Contacts</li>
</ul>

<div id="home" class="tab-content active">
    <h2>Home</h2>
    <p>This is the Home tab content.</p>
</div>

<div id="product" class="tab-content">
    <h2>Product</h2>
    <p>This is the Product tab content. Product details go here.</p>
</div>

<div id="contacts" class="tab-content">
    <h2>Contacts</h2>
    <p>This is the Contacts tab content. Contact information goes here.</p>
</div>

<script>
    // JavaScript function to show the selected tab
    function showTab(tabName) {
        const tabs = document.querySelectorAll('.tab');
        tabs.forEach(tab => tab.classList.remove('active'));

        const tabContents = document.querySelectorAll('.tab-content');
        tabContents.forEach(content => content.classList.remove('active'));

        const selectedTab = document.getElementById(tabName);
        const selectedTabButton = document.querySelector(`.tab[data-tab="${tabName}"]`);

        if (selectedTab && selectedTabButton) {
            selectedTab.classList.add('active');
            selectedTabButton.classList.add('active');
        }
    }
</script>

</body>
</html>
