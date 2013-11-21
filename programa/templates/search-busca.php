 <?php 
/*
	Template Name: Buscas
*/
?>

<?php get_header(); ?>

<script type='text/javascript'>

// Inicia COOKIE para o PHP consumir e executar a curl #gambiarra
api_url = 'http://imoveisemfranca.com.br/';

$location = new String(location);
$location = $location.replace('http://', '');

uri = $location.replace('/busca-de-imoveis/', '').replace('#', '');

URL = api_url + uri;
document.cookie = 'url_return=' + URL;

if("<?php echo $_COOKIE['url_return']; ?>" != URL) {
	window.location.reload();
}

jQuery(document).ready(function() {
	jQuery('#content-estate #flags a, #content-estate #filter-links a').click(function(){
    	url = jQuery(this).attr('href').replace('www.', '');
    	window.location = url;
        return false;
    });
    
    jQuery('#content-estate .paginator a').click(function(){
        url = jQuery(this).attr('href');
    	window.location = url;
        window.location.reload();
        return false;
    });
    
	jQuery("input[name=FINALIDADE]").click(function(){
		jQuery("input[name=FINALIDADE]").removeAttr('checked');
        jQuery(this).attr('checked', '');
	});

   	t_uri = '';
    jQuery('form[name=escolha]').submit(function(){
    	t_uri = '/modo-busca';
        
        if(jQuery('input[name=FINALIDADE]').is(':checked')) {
	        t_uri += '/finalidade-' + jQuery('input[name=FINALIDADE]:checked').val().toLowerCase();
        }
        
        if(jQuery('select[name=CIDADE]').val() != 'CIDADE') {
	        t_uri += '/cidade-' + jQuery('select[name=CIDADE]').val().toLowerCase();
        }

        if(jQuery('select[name=BAIRRO]').val() != 'BAIRRO') {
	        t_uri += '/bairro-' + jQuery('select[name=BAIRRO]').val().toLowerCase();
        }
        
        if(jQuery('select[name=DORMITORIOS]').val() != 'DORMITORIO') {
	        t_uri += '/dormitorios-' + jQuery('select[name=DORMITORIOS]').val().toLowerCase();
        }
        
        if(jQuery('select[name=VALOR]').val() != 'VALOR') {
	        t_uri += '/valor-' + jQuery('select[name=VALOR]').val();
        }
        
        if(jQuery('input[name=CODIGO]').val() != '') {
	        t_uri += '/codigo-' + jQuery('input[name=CODIGO]').val().toLowerCase();
        }
        /*
        if(jQuery('input[name=TEXTO]').val() != '') {
	        t_uri += '/texto-' + jQuery('input[name=TEXTO]').val().toLowerCase();
        }
        */
        
        if(jQuery('select[name=ORDEM]').val() != 'ORDENAR-PESQUISA-POR') {
	        t_uri += '/ordenar-por-' + jQuery('select[name=ORDEM]').val().toLowerCase();
        }
        
        if(t_uri) {
        	// Seta o location e dá um reload na página
        	window.location = "http://<?php echo $_SERVER['HTTP_HOST']; ?>/busca-de-imoveis/#" + t_uri;
           	window.location.reload();
        } else {
        	alert('Para realizar a busca é preciso selecionar algum filtro.');
		}
        
    	return false;
    });
});

</script>


<script type="text/javacsript">

function getCookie(c_name)
{
	var c_value = document.cookie;
	var c_start = c_value.indexOf(" " + c_name + "=");
	if (c_start == -1) {
  		c_start = c_value.indexOf(c_name + "=");
  	}
  	
	if (c_start == -1) {
  		c_value = null;
  	} else {
  		c_start = c_value.indexOf("=", c_start) + 1;
  		var c_end = c_value.indexOf(";", c_start);
  		if (c_end == -1) {
			c_end = c_value.length;
		}

		c_value = unescape(c_value.substring(c_start,c_end));
	}
	return c_value;
}

</script>

<?php

function imoveis($url='', $referer='', $timeout=30, $header='') {

	$api_url = 'http://imoveisemfranca.com.br/';
    $client_url = substr_count($_SERVER['HTTP_HOST'], 'www.') ? $_SERVER['HTTP_HOST'] : str_replace('www.', '', $_SERVER['HTTP_HOST']);
    
	if($_COOKIE['url_return'] == '') {
    	$url = $api_url . $client_url;
    } else {
    	$url = $_COOKIE['url_return'];
	}
    
    if(substr_count($_COOKIE['url_return'], '/pesquisa/') != 0) {
    	$cookie = explode("/pesquisa/", $_COOKIE['url_return']);
        $url = $api_url . '/pesquisa/' . $client_url . '/' . $cookie[1];
    }
    
    if($uri != '') {
    	$url = $base_url . $uri;
	}
    
	if ($referer=='') $referer='http://'. $_SERVER['HTTP_HOST'];
	if(!isset($timeout)) $timeout=30;
    
	$curl = curl_init();
	if(strstr($referer,"://")){
		curl_setopt ($curl, CURLOPT_REFERER, $referer);
	}
	
	curl_setopt ($curl, CURLOPT_URL, $url);
	curl_setopt ($curl, CURLOPT_TIMEOUT, $timeout);
	curl_setopt ($curl, CURLOPT_USERAGENT, sprintf("Mozilla/%d.0",rand(4,5)));
	curl_setopt ($curl, CURLOPT_HEADER, (int)$header);
	curl_setopt ($curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt ($curl, CURLOPT_SSL_VERIFYPEER, 0);
	$html = curl_exec ($curl);
	curl_close ($curl);
    
	return $html;
}
?>


<div id="content-full">
	<div id="hr">
		<div id="hr-center">
			<div id="intro">
				<div class="center-highlight">
					
					<div class="container">
						
						<?php get_template_part('includes/breadcrumbs'); ?>
						
					</div> <!-- end .container -->	
				</div> <!-- end .center-highlight -->
			</div>	<!-- end #intro -->	
		</div> <!-- end #hr-center -->
	</div> <!-- end #hr -->
	
	<div class="center-highlight">
		<div class="container">
			
			<div id="full" class="clearfix">
				
				<?php if (get_option('deepfocus_integration_single_top') <> '' && get_option('deepfocus_integrate_singletop_enable') == 'on') echo(get_option('deepfocus_integration_single_top')); ?>
				<?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
					<div class="entry clearfix post full">
						
						<h1 class="title"><?php the_title(); ?></h1>
						
						<?php the_content(); ?>
						<?php edit_post_link(e