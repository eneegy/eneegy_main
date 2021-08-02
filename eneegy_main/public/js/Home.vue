<template>
<div>
 <div id="head-container">
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light sticky-top">
            <div class="container">
                <a class="navbar-brand" href="/">Eneegy</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#mobile_nav" aria-controls="mobile_nav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span> 
                </button>
                <div class="collapse navbar-collapse" id="mobile_nav">
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0 float-md-right">
                </ul>
                <ul class="navbar-nav navbar-light">
                    <li class="nav-item"><a class="nav-link" href="#">Giới thiệu</a></li>
                    
                    <!--========-->
                    <li class="nav-item"><a class="nav-link" href="/pricing">Bảng giá</a></li>
                    <li class="nav-item dropdown megamenu-li dmenu">
                        <a class="nav-link dropdown-toggle" href="" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Sản phẩm</a>
                        <div class="dropdown-menu megamenu sm-menu border-top" aria-labelledby="dropdown01">
                            <div class="row">
                                <div class="col-sm-6 col-lg-3 border-right mb-4">
                                    <h6>Ecommerce</h6>
                                    <a class="dropdown-item" href="#"><i class="fab fa-magento"></i> Magento Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-magento"></i> Magento 2 Migration</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-magento"></i> Odoo ERP</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-magento"></i> Mobile Commerce</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-magento"></i> CRM for Commerce</a>
                                </div>
                            <div class="col-sm-6 col-lg-3 border-right mb-4">
                                    <h6>LAMP Technology</h6>
                                    <a class="dropdown-item" href="#"><i class="fab fa-php"></i> PHP Website Development</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-circle"></i> Phalcon Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-laravel"></i> Laravel Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-wordpress-simple"></i> WordPress Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-php"></i> Symfony Development</a>
                                </div>
                                <div class="col-sm-6 col-lg-3 border-right mb-4">
                                    <h6>Mobile</h6>
                                    <a class="dropdown-item" href="#"><i class="fab fa-apple"></i> iPhone App Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-android"></i> Android App Development</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-mobile-alt"></i> Phone Gap App Development</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-tablet-alt"></i> Hybrid App Development</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-mobile-alt"></i> Ionic Development</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-tablet-alt"></i> React Native Development</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-mobile-alt"></i> Xamarin App Development</a>
                                </div>
                                <div class="col-sm-6 col-lg-3 mb-4">
                                    <h6>Node.js & MongoDB</h6>
                                    <a class="dropdown-item" href="#"><i class="fas fa-cubes"></i> Full Stack Development</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-cube"></i> MEAN Stack</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-angular"></i> AngularJS</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-node-js"></i> Node.JS Development</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-leaf fa-rotate-90"></i> MongoDB Development</a>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-sm-6 col-lg-3 border-right mb-4">
                                    <h6>Microsoft Technology</h6>
                                    <a class="dropdown-item" href="#"><i class="fab fa-windows"></i> Microsoft App Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-windows"></i> MS Desktop App Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-windows"></i> SharePoint Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-windows"></i> ASP.NET Development</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-windows"></i> CMS Development</a>
                                </div>
                            <div class="col-sm-6 col-lg-3 border-right mb-4">
                                    <h6>Cloud Services</h6>
                                    <a class="dropdown-item" href="#"><i class="fas fa-cloud"></i> DevOps</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-amazon"></i> Amazon Web Services</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-windows"></i> Azure Cloud Service</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-google"></i> Google App Engine Services</a>
                                </div>
                                <div class="col-sm-6 col-lg-3 border-right mb-4">
                                    <h6>Enterprise Services</h6>
                                    <a class="dropdown-item" href="#"><i class="fas fa-laptop"></i> Augmented Reality</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-laptop"></i> CRM</a>
                                    <a class="dropdown-item" href="#"><i class="fab fa-buromobelexperte"></i> Enterprise Mobility Services</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-th-large"></i> Blockchain Services</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-briefcase"></i> Business Intelligence</a>
                                </div>
                                <div class="col-sm-6 col-lg-3 mb-4">
                                    <h6>Digital Marketing</h6>
                                    <a class="dropdown-item" href="#"><i class="fas fa-laptop"></i> Digital Marketing</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-laptop"></i> PPC Management Services</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-laptop"></i> E-commerce SEO Services</a>
                                    <a class="dropdown-item" href="#"><i class="fas fa-laptop"></i> Conversion Rate Optimization</a>
                                </div>
                            </div>
                        </div>
                    </li>
                    <!--=========-->
                    
                    <li class="nav-item dmenu dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Hỗ trợ
                        </a>
                        <div class="dropdown-menu sm-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="#">Software Development</a>
                            <a class="dropdown-item" href="#">Web Designing & Development</a>
                            <a class="dropdown-item" href="#">Mobile Application</a>
                            <a class="dropdown-item" href="#">Business Solutions & Business Process</a>
                            <a class="dropdown-item" href="#">Digital Marketing & SEO Services</a>
                            <a class="dropdown-item" href="#">Web Hosting & Maintenance</a>
                            <a class="dropdown-item" href="#">Cyber Security</a>
                            <a class="dropdown-item" href="#">Block Chain Implementation</a>
                            <a class="dropdown-item" href="#">Big Data</a>
                        </div>
                    </li>
                    <li class="nav-item"><a class="nav-link" href="<?php echo siteURL;?>contact-us.php">Đăng nhập</a></li>   
                </ul>
                </div>
            </div>
        </nav>
            <header class="masthead">
                <div class="container h-100" style="margin-top: -80px;">
                    <div class="row h-100">
                        <div class="col-lg-12 d-lg-flex my-auto justify-content-lg-center">
                            <div class="header-content">
                                <div class="d-lg-flex justify-content-lg-center"><img class="d-lg-flex justify-content-lg-center" id="hero-logo" src="assets/eneegy_main/img/light.svg" width="64px" height="64px" style="justify-content: center!important;"></div>
                                <h5 class="mb-5" style="font-family: Lato, sans-serif;font-weight: normal;text-align: center;">Eneegy giúp bạn quản lý cơ sở kinh doanh của mình trong một thế giới luôn chuyển động và thay đổi!</h5>
                                <div class="d-flex"><a class="btn btn-outline-primary btn-xl js-scroll-trigger" role="button" href="#download" style="float: left;/*width: 400px;*/margin: 0px auto;">Dùng thử ngay</a></div>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        </div>
    </div>
    <section id="download" class="download text-center bg-primary">
        <div class="container">
            <div class="row">
                <div class="col-md-8 mx-auto">
                    <h2 class="text-dark section-heading">Tất cả đều xoay quanh việc kinh doanh của bạn&nbsp;</h2>
                    <p class="text-dark">Chúng tôi đặt bạn ở trung tâm mỗi khi ra quyết định hay phải lựa chọn giữa các tính năng cần phát triển</p>
                    <div></div>
                </div>
            </div>
        </div>
    </section>
    <section id="features" class="features">
        <div class="container">
            <div class="section-heading text-center">
                <h2>Không giới hạn tính năng.<span>&nbsp;Chi trả dễ dàng.</span></h2>
                <p class="text-muted">Tất cả mọi tính năng được cung cấp trong các gói chi trả theo tháng.</p>
                <hr>
            </div>
            <div class="row">
                <div class="col-lg-4 my-auto">
                    <div class="device-container">
                        <div class="device-mockup iphone6_plus portrait white">
                            <div class="device" style="background-image:url('assets/eneegy_main/img/iphone_6_plus_white_port.png');">
                                <div class="screen"><img class="img-fluid" src="assets/eneegy_main/img/demo-screen-1.jpg"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-8 my-auto">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="feature-item"><i class="icon-screen-smartphone text-primary"></i>
                                    <h3>Làm việc từ xa</h3>
                                    <p class="text-muted">Hệ thống của chúng tôi thân thiện với thiết bị di động. Bạn có thể truy cập từ bất kì đâu có Internet.</p>
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="feature-item"><i class="icon-camera text-primary"></i>
                                    <h3>Tùy biến</h3>
                                    <p class="text-muted">Bla bla bla bla bla bla bla bla bla lba bla bla</p>
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="feature-item"><i class="icon-present text-primary"></i>
                                    <h3>Linh Động</h3>
                                    <p class="text-muted">Bla Bla Bla!</p>
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <div class="feature-item"><i class="icon-lock-open text-primary"></i>
                                    <h3>Nguồn mở</h3>
                                    <p class="text-muted">Bla Bla Bla</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="cta" style="background-image:url('assets/eneegy_main/img/bg-cta.jpg');">
        <div class="cta-content">
            <div class="container">
                <h2>LÀM VIỆC TỪ XA.<br>BẤT CỨ LÚC NÀO.<br></h2><a class="btn btn-outline-warning btn-xl js-scroll-trigger" role="button" href="#contact">bẮT ĐẦU</a>
            </div>
        </div>
        <div class="overlay"></div>
    </section>
    <section id="contact" class="contact bg-primary">
        <div class="container">
            <h2><span>Chúng tôi&nbsp;</span><i class="fa fa-heart"></i><span>&nbsp;kết bạn!</span></h2>
            <ul class="list-inline list-social" style="height: 48px;">
                <li class="list-inline-item social-twitter"><a href="#" style="width: 48px;height: 48px;"><i class="fa fa-twitter"></i></a></li>
                <li class="list-inline-item social-facebook" style="width: 48px;"><a href="#"><i class="fa fa-facebook"></i></a></li>
                <li class="list-inline-item social-google-plus"><a href="#"><i class="fa fa-youtube-play"></i></a></li>
            </ul>
        </div>
    </section>
    <footer class="footer section pt-6 pt-md-8 pt-lg-10 pb-3 bg-primary text-white overflow-hidden">
    <div class="pattern pattern-soft top"></div>
    <div class="container">
        <div class="row">
            <div class="col-lg-4 mb-4 mb-lg-0">
                <a class="footer-brand mr-lg-5 d-flex" href="index.html">
                    <img src="assets/eneegy_main/img/light.svg" height="36" class="mr-3" alt="Footer logo">
                </a>
                <p class="my-4">Giúp bạn quản lí và phát triển doanh nghiệp trong một thế giới luôn chuyển động.</p>
                <div class="dropdown mb-4 mb-lg-0">
                    <a id="langsDropdown" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle footer-language-link">
                        <img src="./front/assets/eneegy_main/img/flags/vietnam.svg" alt="Vietnam Flag" class="language-flag"> Tiếng Việt<i class="fas fa-chevron-down ml-1"></i>
                    </a>
                    <div aria-labelledby="langsDropdown" class="dropdown-menu dropdown-menu-center">
                        <a href="#" class="dropdown-item text-gray text-sm"><img src="./front/assets/eneegy_main/img/flags/united-states-of-america.svg" alt="USA Flag" class="language-flag"> English</a>
                    </div>
                </div>
            </div>
            <div class="col-6 col-sm-3 col-lg-2 mb-4 mb-lg-0">
                <h6>Eneegy</h6>
                <ul class="links-vertical">
                    <li><a target="_blank" href="#">Giá cả</a></li>
                    <li><a target="_blank" href="#">Nhật kí</a></li>
                    <li><a target="_blank" href="#">Giới thiệu</a></li>
                </ul>
            </div>
            <div class="col-6 col-sm-3 col-lg-2 mb-4 mb-lg-0">
                <h6>Trợ giúp</h6>
                <ul class="links-vertical">
                    <li><a target="_blank" href="#">Thẻ</a></li>
                    <li><a target="_blank" href="#">Tài liệu</a></li>
                    <li><a target="_blank" href="#">Liên hệ</a></li>
                </ul>
            </div>
            <div class="col-12 col-sm-6 col-lg-4">
                <h6>Nhận Email</h6>
                <p class="font-small">Nhận thông tin mới nhất về Eneegy qua email của bạn.</p>
                <form action="#">
                    <div class="form-row">
                        <div class="col-8">
                            <input type="email" class="form-control mb-2" placeholder="Email Address" name="email" required="">
                        </div>
                        <div class="col-4">
                            <button type="submit" class="btn btn-secondary btn-block"><span>Đăng kí</span></button>
                        </div>
                    </div>
                </form>
                <small class="mt-2 form-text">Chúng tôi bảo vệ dữ liệu của bạn. Xem <a href="#" class="font-weight-bold text-underline">Điều khoản bảo mật</a></small>
            </div>
        </div>
        <hr class="my-4 my-lg-5">
        <div class="row">
            <div class="col pb-4 mb-md-0">
                <div class="d-flex text-center justify-content-center align-items-center">
                    <p class="font-weight-normal mb-0">© Eneegy <span class="current-year">2021</span>. All rights reserved.</p>
                </div>
            </div>
        </div>
    </div>
</footer>
</div>
</template>

<script>
export default ({
    data() {
       return {name: 'Vue'}
    }
})
</script>
