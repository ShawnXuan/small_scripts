function c = GetFundamentalClasses(v, vn='', l=0)
%http://www.mathworks.com/help/matlab/matlab_prog/fundamental-matlab-classes.html
    if strcmp(vn, '')
        vn = inputname(1);
    end
    cov=class(v);%class of v
    b='';
    for i = 1:l
        b=['    ' b];
    end
    %fprintf("%s%s:%s",b,vn, cov)    
    [r, c] = size(v);
    switch cov
        case 'struct'            
            fn = fieldnames(v);
            fprintf("%s%s:%s\n",b,vn, cov)   
            for f = fn'
                %getfield(v,f{1,1})
                GetFundamentalClasses(getfield(v,f{1,1}),f{1,1},l+1);
            end
        case 'cell'
            fprintf("%s%s:%s",b,vn, cov) 
            fprintf('[%dx%d]\n',r,c)
            for i=1:r
                for j=1:c
                    s=['cell(' int2str(i) ',' int2str(j) ')'];
                    GetFundamentalClasses(v{i,j},s,l+1);
                end
            end
        case {'double', 'single'}
            if r*c>1
                fprintf('%s%s:%s[%dx%d]\n',b,vn, cov,r,c)    
            else
                fprintf('%s%s=%f\n',b,vn, v)%cov   
            end 
        case 'char'
            if r*c>1
                fprintf('%s%s:%s[%dx%d]\n',b,vn, cov,r,c)    
            else
                fprintf("%s%s='%s'\n",b,vn, v)%cov
            end
        case {'table', 'logical','function_handle'}
            %do nothing currently
        otherwise
            if r*c>1
                fprintf('%s%s:%s[%dx%d]\n',b,vn, cov,r,c)    
            else
                fprintf('%s%s=%d\n',b,vn, v)%cov   
            end            
    end
    
