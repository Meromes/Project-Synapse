%% instantiate the library
disp('Loading the library...');
lib = lsl_loadlib();

% resolve a stream...
disp('Resolving an EEG stream...');
result = {};
while isempty(result)
    result = lsl_resolve_byprop(lib,'type','EEG'); end

% create a new inlet
disp('Opening an inlet...');
inlet = lsl_inlet(result{1});

disp('Now receiving data...');
while true
% get data from the inlet
[vec1,ts1] = inlet.pull_sample();
[vec2,ts2] = inlet.pull_sample();
[vec3,ts3] = inlet.pull_sample();
[vec4,ts4] = inlet.pull_sample();
[vec5,ts5] = inlet.pull_sample();
[vec6,ts6] = inlet.pull_sample();
[vec7,ts7] = inlet.pull_sample();
[vec8,ts8] = inlet.pull_sample();
% and display it
fprintf('%.2f\t',vec1);
fprintf('\n');
fprintf('%.2f\t',vec2);
fprintf('\n');
fprintf('%.2f\t',vec3);
fprintf('\n');
fprintf('%.2f\t',vec4);
fprintf('\n');
fprintf('%.2f\t',vec5);
fprintf('\n');
fprintf('%.2f\t',vec6);
fprintf('\n');
fprintf('%.2f\t',vec7);
fprintf('\n');
fprintf('%.2f\t',vec8);
fprintf('\n');

M1=mean(vec1);
M2=mean(vec2);
M3=mean(vec3);
M4=mean(vec4);
M5=mean(vec5);
M6=mean(vec6);
M7=mean(vec7);
M8=mean(vec8);

fprintf('%.2f\t\n',M1);
fprintf('%.2f\t\n',M2);
fprintf('%.2f\t\n',M3);
fprintf('%.2f\t\n',M4);
fprintf('%.2f\t\n',M5);
fprintf('%.2f\t\n',M6);
fprintf('%.2f\t\n',M7);
fprintf('%.2f\t\n',M8);
end
