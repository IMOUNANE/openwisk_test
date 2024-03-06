<?php
function main(array $params): array
{
    $initialValue = json_decode($params["initialValue"], true);
    $result = json_decode($params["secondValue"], true); 

    $original = $result / 2;

    return  ["final_result" => "oh, no this is last script. result: ". $result,"origin" => $original];
}
?>
