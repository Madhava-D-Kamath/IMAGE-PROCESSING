
% ---------------------------------
% Step 1: Clear workspace
% ---------------------------------
clc;
clear;
close all;

% ---------------------------------
% Step 2: Read the image
% ---------------------------------
img = imread('car.jpg');   % Change file name if needed %[output:6f49e14d]

% ---------------------------------
% Step 3: Display original image
% ---------------------------------
figure;
imshow(img);
title('Original Image');

% ---------------------------------
% Step 4: Convert to double for processing
% ---------------------------------
img_double = im2double(img);

% ---------------------------------
% Step 5: Adjust contrast
% ---------------------------------
alpha = 1.3;   % Contrast factor (1.0 - 3.0)
beta = 0.2;    % Brightness factor (0 - 1)

enhanced = alpha * img_double + beta;

% ---------------------------------
% Step 6: Clip values between 0 and 1
% ---------------------------------
enhanced = min(max(enhanced, 0), 1);

% ---------------------------------
% Step 7: Display enhanced image
% ---------------------------------
figure;
imshow(enhanced);
title('Enhanced Image');

% ---------------------------------
% Step 8: Save enhanced image
% ---------------------------------
imwrite(enhanced, 'enhanced_car.jpg');


%[appendix]{"version":"1.0"}
%---
%[metadata:view]
%   data: {"layout":"onright","rightPanelPercent":14}
%---
%[output:6f49e14d]
%   data: {"dataType":"error","outputData":{"errorType":"runtime","text":"Error using <a href=\"matlab:matlab.lang.internal.introspective.errorDocCallback('imread>get_full_filename', '\/MATLAB\/toolbox\/matlab\/matlab_im\/imread.m', 635)\" style=\"font-weight:bold\">imread>get_full_filename<\/a> (<a href=\"matlab: opentoline('\/MATLAB\/toolbox\/matlab\/matlab_im\/imread.m',635,0)\">line 635<\/a>)\nUnable to find file \"car.jpg\".\n\nError in <a href=\"matlab:matlab.lang.internal.introspective.errorDocCallback('imread', '\/MATLAB\/toolbox\/matlab\/matlab_im\/imread.m', 395)\" style=\"font-weight:bold\">imread<\/a> (<a href=\"matlab: opentoline('\/MATLAB\/toolbox\/matlab\/matlab_im\/imread.m',395,0)\">line 395<\/a>)\n        fullname = get_full_filename(filename);\n        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"}}
%---
