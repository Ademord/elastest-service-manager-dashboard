
<!DOCTYPE html>
<html lang="en">
<head>
    @include('includes.head')
    <script src="https://code.jquery.com/jquery-1.11.1.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
</head>

<body class="">
    <div class="wrapper">
        @include('includes.header')

        <div class="main-panel">
            <div class="content">
                <div class="container-fluid">
                    @yield('content')
                </div>
            </div>

            <br>
            @include('includes.footer')
        </div>
    </div>
</body>
</html>